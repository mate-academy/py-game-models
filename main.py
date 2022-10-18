import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    pass
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        else:
            race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if info["guild"]:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=info["guild"]["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
