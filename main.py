import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json

FILE_NAME = "players.json"


def main():
    with open(FILE_NAME, "r") as players:
        players_info = json.load(players)
        print(players_info)

    for info in players_info.values():

        if not Race.objects.filter(name=info["race"]["name"]).exists():
            race = Race.objects.create(name=info["race"]["name"],
                                       description=info["race"]["description"])
        else:
            race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(name=skill["name"],
                                             bonus=skill["bonus"],
                                             race=race)

        if info["guild"] is None:
            guild = None

        elif not Guild.objects.filter(name=info["guild"]["name"]).exists():
            guild = Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )
        else:
            guild = Guild.objects.get(name=info["guild"]["name"])

    for player_name, info in players_info.items():
        Player.objects.create(
            nickname=player_name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
