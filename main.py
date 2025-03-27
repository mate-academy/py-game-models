import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data_file:
        players_data = json.load(data_file)

    for player, data in players_data.items():
        if not Race.objects.filter(name=data["race"]["name"]):
            race = Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )
        else:
            race = Race.objects.get(name=data["race"]["name"])

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if data["guild"]:
            if not Guild.objects.filter(name=data["guild"]["name"]):
                guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=data["guild"]["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
