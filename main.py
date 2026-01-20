import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player

import json
from pathlib import Path


def main() -> None:
    json_path = Path("players.json")

    # Read JSON file safely
    with json_path.open("r", encoding="utf-8") as file:
        players_data = json.load(file)

    # Iterate through JSON dict: nickname → player data
    for nickname, data in players_data.items():
        race_info = data.get("race", {})  # safe fallback to {}
        race_name = race_info.get("name")
        race_desc = race_info.get("description") or ""

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc},
        )

        # Handle skills (may be missing or empty)
        skills_info = race_info.get("skills", [])
        for skill_info in skills_info:
            Skill.objects.get_or_create(
                name=skill_info.get("name"),
                defaults={
                    "bonus": skill_info.get("bonus"),
                    "race": race,
                },
            )

        # Process guild (nullable)
        guild_info = data.get("guild")
        guild_obj = None
        if guild_info:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")},
            )

        # Create player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
