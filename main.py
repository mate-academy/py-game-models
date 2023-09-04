import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for name, info in players.items():

        if info["guild"] is not None:
            Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

            Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=info["race"]["name"])
                )

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=info["race"]["name"]),
            guild=(
                Guild.objects.get(name=info["guild"]["name"])
                if info["guild"] is not None else None)
        )


if __name__ == "__main__":
    main()
