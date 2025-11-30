import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, data in players.items():
        race_data = data.get("race")
        if not race_data:
            raise ValueError(f'Player "{name}" has no race defined.')

        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description", "")
            }
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race_obj,
                defaults={
                    "bonus": skill.get("bonus")
                }
            )

        guild_data = data.get("guild")
        guild_obj = None

        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
