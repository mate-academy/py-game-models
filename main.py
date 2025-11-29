import json
from pathlib import Path

from db.models import Guild, Player, Race, Skill


def _iter_players(raw: object) -> list[dict]:
    """
    Normaliza players.json para uma lista de dicts e garante 'nickname'.
    Aceita formatos:
    - [ {...}, {...} ]
    - { "players": [ {...}, {...} ] }
    - { "players": { "nick1": {...}, "nick2": {...} } }
    - { "nick1": {...}, "nick2": {...} }
    """

    def _ensure_item(nick_key: str | None, item: object) -> dict:
        if not isinstance(item, dict):
            raise TypeError("Each player entry must be an object/dict")
        out = dict(item)  # não muta o original
        if "nickname" not in out:
            out["nickname"] = nick_key or out.get("name", "")
        return out

    if isinstance(raw, list):
        return [_ensure_item(None, it) for it in raw]

    if isinstance(raw, dict):
        if "players" in raw:
            players_obj = raw["players"]
            if isinstance(players_obj, list):
                return [_ensure_item(None, it) for it in players_obj]
            if isinstance(players_obj, dict):
                return [_ensure_item(nk, it) for nk, it in players_obj.items()]
            raise TypeError("Invalid 'players' value in players.json")

        # Ex.: { "Legolas": {...}, "Gimli": {...} }
        return [_ensure_item(nk, it) for nk, it in raw.items()]

    raise TypeError("Unsupported players.json format")


def _as_race(race_data: object) -> Race:
    if isinstance(race_data, dict):
        name = race_data.get("name", "")
        description = race_data.get("description", "")
    else:
        name = str(race_data)
        description = ""
    race, created = Race.objects.get_or_create(
        name=name,
        defaults={"description": description},
    )
    # Atualiza descrição se vier depois com valor melhor
    if not created and description and race.description != description:
        race.description = description
        race.save(update_fields=["description"])
    return race


def _as_guild(guild_data: object) -> Guild | None:
    if guild_data is None:
        return None
    if isinstance(guild_data, dict):
        name = guild_data.get("name", "")
        description = guild_data.get("description")
        guild, created = Guild.objects.get_or_create(
            name=name,
            defaults={"description": description},
        )
        if not created and description is not None:
            if guild.description != description:
                guild.description = description
                guild.save(update_fields=["description"])
        return guild
    name = str(guild_data)
    guild, _ = Guild.objects.get_or_create(name=name)
    return guild


def _ensure_skills(skills_data: object, race: Race) -> None:
    if not isinstance(skills_data, list):
        return
    for item in skills_data:
        if isinstance(item, dict):
            name = item.get("name", "")
            bonus = item.get("bonus", "")
            # Atualiza bonus/race se a skill já existir
            Skill.objects.update_or_create(
                name=name,
                defaults={"bonus": bonus, "race": race},
            )
        else:
            # Se vier só o nome, não sobrescreve bonus existente
            name = str(item)
            Skill.objects.get_or_create(
                name=name,
                defaults={"bonus": "", "race": race},
            )


def _ensure_global_skills(raw: object) -> None:
    """Cria skills definidas em blocos globais ('skills'/'races')."""
    if not isinstance(raw, dict):
        return

    # Caso A: bloco global "skills"
    if "skills" in raw:
        skills_block = raw["skills"]
        # A1) lista de skills; cada skill deve indicar a raça
        if isinstance(skills_block, list):
            for skill_def in skills_block:
                if not isinstance(skill_def, dict):
                    continue
                race_data = skill_def.get("race")
                if race_data is None:
                    continue
                race = _as_race(race_data)
                skill_payload = [{
                    "name": skill_def.get("name", ""),
                    "bonus": skill_def.get("bonus", ""),
                }]
                _ensure_skills(skill_payload, race)

        # A2) dict mapeando raça -> lista de skills
        elif isinstance(skills_block, dict):
            for race_key, skills_list in skills_block.items():
                race = _as_race(race_key)
                _ensure_skills(skills_list, race)

    # Caso B: bloco "races" com skills dentro
    if "races" in raw:
        races_obj = raw["races"]
        # B1) lista de raças com 'skills'
        if isinstance(races_obj, list):
            for race_def in races_obj:
                if not isinstance(race_def, dict):
                    continue
                race = _as_race(race_def)
                _ensure_skills(race_def.get("skills", []), race)
        # B2) dict nome_da_raça -> { description, skills }
        elif isinstance(races_obj, dict):
            for race_name, race_data in races_obj.items():
                if isinstance(race_data, dict):
                    race = _as_race({
                        "name": race_name,
                        "description": race_data.get("description", ""),
                    })
                    _ensure_skills(race_data.get("skills", []), race)
                else:
                    race = _as_race(race_name)
                    _ensure_skills([], race)


def main() -> None:
    """
    Lê players.json (ao lado de main.py) e popula o banco:
    - garante unicidade de Race, Guild e Skill
    - cria Player se ainda não existir pelo nickname
    """
    data_path = Path(__file__).with_name("players.json")
    with data_path.open(encoding="utf-8") as f:
        raw = json.load(f)

    # 1) Skills em blocos globais (se houver)
    _ensure_global_skills(raw)

    # 2) Players
    players = _iter_players(raw)

    for entry in players:
        race_data = entry.get("race")
        race = _as_race(race_data)

        # skills declaradas dentro da race do próprio player
        if isinstance(race_data, dict) and "skills" in race_data:
            _ensure_skills(race_data.get("skills", []), race)

        # skills declaradas diretamente no player
        _ensure_skills(entry.get("skills", []), race)

        guild = _as_guild(entry.get("guild"))

        Player.objects.get_or_create(
            nickname=entry["nickname"],
            defaults={
                "email": entry["email"],
                "bio": entry["bio"],
                "race": race,
                "guild": guild,
            },
        )
