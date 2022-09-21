import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main():
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:

        if not Race.objects.filter(
                name=players[player]["race"]["name"]).exists():
            Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"])

            for skill in players[player]["race"]["skills"]:

                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(
                            name=players[player]["race"]["name"]))

        if not players[player]["guild"]:
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]))

        else:
            if not Guild.objects.filter(
                    name=players[player]["guild"]["name"]).exists():
                if players[player]["guild"]["description"] is None:

                    Guild.objects.create(
                        name=players[player]["guild"]["name"])
                else:
                    Guild.objects.create(
                        name=players[player]["guild"]["name"],
                        description=players[player]["guild"]["description"])
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]),
                guild=Guild.objects.get(name=players[player]["guild"]["name"]))


if __name__ == "__main__":
    main()
