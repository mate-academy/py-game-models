import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main():
    with open("players.json", "r") as file:
        players = json.load(file)

    for player in players:

        if not Race.objects.filter(
                name=players[player]["race"]["name"]).exists():
            race = Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"])
            race.save()

            for skill in players[player]["race"]["skills"]:

                if not Skill.objects.filter(name=skill["name"]).exists():
                    skill = Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(
                            name=players[player]["race"]["name"]))
                    skill.save()

        if not players[player]["guild"]:
            player = Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]))

            player.save()
        else:
            if not Guild.objects.filter(
                    name=players[player]["guild"]["name"]).exists():
                if players[player]["guild"]["description"] is None:

                    guild = Guild.objects.create(
                        name=players[player]["guild"]["name"])
                    guild.save()
                else:
                    guild = Guild.objects.create(
                        name=players[player]["guild"]["name"],
                        description=players[player]["guild"]["description"])
                    guild.save()
            player = Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=Race.objects.get(name=players[player]["race"]["name"]),
                guild=Guild.objects.get(name=players[player]["guild"]["name"]))
            player.save()


if __name__ == "__main__":

    main()
