import json
from typing import NoReturn

from db.models import Race, Guild, Skill, Player


def main() -> NoReturn:
    with open("db/data.json", encoding="utf-8") as file:
        data = json.load(file)

    for race_name, race_data in data["races"].items():
        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_data.get("description", "")}
        )

        for skill_name, bonus in race_data.get("skills", {}).items():
            Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": bonus, "race": race_obj}
            )

    for guild_name, guild_data in data["guilds"].items():
        Guild.objects.get_or_create(
            name=guild_name,
            defaults={"description": guild_data.get("description")}
        )

    for _, player_data in data["players"].items():
        race_obj = Race.objects.get(name=player_data["race"])
        guild_name = player_data.get("guild")
        guild_obj = Guild.objects.get(name=guild_name) if guild_name else None

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race_obj,
                "guild": guild_obj,
            }
        )
