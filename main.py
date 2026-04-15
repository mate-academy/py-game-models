import json
from pathlib import Path
from typing import Any

import init_django_orm  # noqa: F401
from db.models import Guild, Player, Race, Skill


def _extract_players(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]

    if isinstance(data, dict):
        players = data.get("players")
        if isinstance(players, list):
            return [item for item in players if isinstance(item, dict)]

        extracted_players: list[dict[str, Any]] = []
        for nickname, player_data in data.items():
            if isinstance(player_data, dict):
                normalized_player = dict(player_data)
                normalized_player.setdefault("nickname", nickname)
                extracted_players.append(normalized_player)

        return extracted_players

    return []


def _get_race_data(player_data: dict[str, Any]) -> dict[str, Any]:
    race_data = player_data.get("race")

    if isinstance(race_data, dict):
        return race_data

    if isinstance(race_data, str):
        return {
            "name": race_data,
            "description": "",
            "skills": player_data.get("skills", []),
        }

    return {
        "name": "",
        "description": "",
        "skills": [],
    }


def main() -> None:
    file_path = Path("players.json")

    with file_path.open("r", encoding="utf-8") as file:
        data: Any = json.load(file)

    players_data = _extract_players(data)

    for player_data in players_data:
        nickname = player_data.get("nickname")
        email = player_data.get("email", "")
        bio = player_data.get("bio", "")

        if not nickname:
            continue

        race_data = _get_race_data(player_data)
        race_name = race_data.get("name")

        if not race_name:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "description": race_data.get("description", ""),
            },
        )

        skills_data = race_data.get("skills", [])
        if isinstance(skills_data, list):
            for skill_data in skills_data:
                if not isinstance(skill_data, dict):
                    continue

                skill_name = skill_data.get("name")
                if not skill_name:
                    continue

                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "bonus": skill_data.get("bonus", ""),
                        "race": race,
                    },
                )

        guild = None
        guild_data = player_data.get("guild")

        if isinstance(guild_data, dict):
            guild_name = guild_data.get("name")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={
                        "description": guild_data.get("description"),
                    },
                )
        elif isinstance(guild_data, str) and guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data,
                defaults={
                    "description": None,
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
