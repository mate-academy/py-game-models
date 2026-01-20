import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        data = json.load(data_file)

    for name, attributes in data.items():
        race, created = Race.objects.get_or_create(
            name=attributes["race"]["name"],
            description=(
                attributes["race"]["description"]
                if attributes["race"]["description"]
                else None
            )
        )
        if created:
            skills = attributes["race"].get("skills")
            if skills:
                for skill in skills:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        guild = attributes.get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=attributes["guild"]["name"],
                description=(
                    attributes["guild"]["description"]
                    if attributes["guild"]["description"]
                    else None
                )
            )

        Player.objects.create(
            nickname=name,
            email=attributes["email"],
            bio=attributes["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
