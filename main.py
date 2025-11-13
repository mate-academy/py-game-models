import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player

import json
from pathlib import Path


def main() -> None:
    json_path = Path("players.json")

    # Step 1: Read JSON
    with json_path.open("r", encoding="utf-8") as file:
        players_data = json.load(file)

    # Step 2: Process data
    for nickname, data in players_data.items():
        race_info = data["race"]

        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description") or ""},
        )

        # Skills
        for skill_info in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={
                    "bonus": skill_info["bonus"],
                    "race": race,
                },
            )

        # Guild (may be null)
        guild_info = data.get("guild")
        guild_obj = None
        if guild_info:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")},
            )

        # Create player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
