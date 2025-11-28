import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, entry in data.items():
        race_name = entry["race"]["name"]
        race_desc = entry["race"].get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc}
        )

        for skill_data in entry["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        guild_obj = None
        guild_data = entry.get("guild")

        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": entry["email"],
                "bio": entry["bio"],
                "race": race,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
