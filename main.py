import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for value in players.values():
        if value["guild"] is not None:
            if not Guild.objects.filter(name=value["guild"]["name"]).exists():
                Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )

    for value in players.values():
        if not Race.objects.filter(name=value["race"]["name"]).exists():
            Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )

    for value in players.values():
        for skill in value["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=value["race"]["name"])
                )

    for name, value in players.items():
        Player.objects.create(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=Race.objects.get(name=value["race"]["name"]),
            guild=(
                Guild.objects.get(name=value["guild"]["name"])
                if value["guild"] is not None else None)
        )


if __name__ == "__main__":
    main()
