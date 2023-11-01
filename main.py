import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        print(data)
    for player, info in data.items():
        Player(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get_or_create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            ),
            guild=Guild.objects.get_or_create(
                name=info["guild"]["name"],
                desription=info["guild"]["description"]
            ),
        )
        for race in info["race"]:
            Skill(
                name=race["skills"]["bonus"],
                bonus=race["skills"]["bonus"],
                race=Race.objects.get_or_create(
                    name=race["name"],
                )
            )


if __name__ == "__main__":
    main()
