import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, pdata in players_data.items():
        if not isinstance(pdata, dict):
            continue

        race_info = pdata.get("race") or {}
        race_name = race_info.get("name")
        if not race_name:
            continue

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_info.get("description", "")}
        )

        for skill in race_info.get("skills", []) or []:
            if not isinstance(skill, dict):
                continue
            skill_name = skill.get("name")
            if not skill_name:
                continue
            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": skill.get("bonus", ""),
                    "race": race_obj
                }
            )

        guild_obj = None
        guild_info = pdata.get("guild")
        if isinstance(guild_info, dict) and guild_info.get("name"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata.get("email", ""),
                "bio": pdata.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            }
        )
