import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name, info in data.items():
        name = name
        email = info["email"]
        bio = info["bio"]
        race = info["race"]
        guild = info["guild"]
        skills = race["skills"]

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
        race = Race.objects.get(name=race["name"])

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            guild = Guild.objects.get(name=guild["name"])
        else:
            guild = None

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if not Player.objects.filter(nickname=name):
            Player.objects.create(
                nickname=name,
                email=email,
                bio=bio,
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
