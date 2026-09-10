import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for key, value in data.items():
        obj_race, created_race = Race.objects.get_or_create(
            name=value["race"].get("name"),
            defaults={
                "description": value["race"].get("description")
            }
        )

        for skills in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills.get("name"),
                defaults={
                    "bonus": skills.get("bonus"),
                    "race": obj_race
                }
            )

        if value["guild"] is not None:
            obj_guild, created_guild = Guild.objects.get_or_create(
                name=value["guild"].get("name"),
                defaults={
                    "description": value["guild"].get("description")
                }
            )
        else:
            obj_guild = None

        Player.objects.create(
            nickname=key,
            email=value.get("email"),
            bio=value.get("bio"),
            race=obj_race,
            guild=obj_guild
        )


if __name__ == "__main__":
    main()
