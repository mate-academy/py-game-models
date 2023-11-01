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
            )[0],
            guild=Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )[0] if info["guild"] else info["guild"],
        )
        race_name = info["race"]["name"]
        for race in info["race"]["skills"]:
            Skill(
                name=race["name"],
                bonus=race["bonus"],
                race=Race.objects.get_or_create(
                    name=race_name,
                )[0]
            )


if __name__ == "__main__":
    main()
