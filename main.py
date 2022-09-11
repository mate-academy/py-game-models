import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as players_saves:
        players = json.load(players_saves)

    for player in players:
        if players[player]["guild"] is None:
            guild = None
        elif not Guild.objects.filter(
                name=players[player]["guild"]["name"]
        ).exists():
            Guild.objects.create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"])
            guild = Guild.objects.get(name=players[player]["guild"]["name"])
        if not Race.objects.filter(
                name=players[player]["race"]["name"]
        ).exists():
            Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]
            )
        race = Race.objects.get(name=players[player]["race"]["name"])
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=race,
                guild=guild
            )
        for skill in players[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
