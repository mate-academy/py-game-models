import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main():
    with open("players.json") as players_list:
        gamers = json.load(players_list)
    for player in gamers:
        if not Race.objects.filter(
                name=gamers[player]["race"]["name"]).exists():
            race_gamer = Race.objects.create(
                name=gamers[player]["race"]["name"],
                description=gamers[player]["race"]["description"])

        skills = gamers[player]["race"]["skills"]
        for skill in skills:
            if not Skill.objects.filter(
                    name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race_gamer)
        if gamers[player]["guild"] is None:
            guild_gamer = None
        else:
            if not Guild.objects.filter(
                    name=gamers[player]["guild"]["name"]).exists():
                guild_gamer = Guild.objects.create(
                    name=gamers[player]["guild"]["name"],
                    description=gamers[player]["guild"]["description"])
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=gamers[player]["email"],
                bio=gamers[player]["bio"],
                race=race_gamer,
                guild=guild_gamer)


if __name__ == "__main__":
    main()
