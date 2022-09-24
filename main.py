import django.db.utils

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    with open("players.json", "r") as players:
        players = json.load(players)

    # Filling in the Race table
    for player in players:
        try:
            Race.objects.create(
                name=f'{players[player]["race"]["name"]}',
                description=f'{players[player]["race"]["description"]}'
            )
        except django.db.utils.IntegrityError:
            continue

    # Filling in the Skill table
    for player in players:
        try:
            player_temp = players[player]["race"]["skills"]
            if len(players[player]["race"]["skills"]) != 0:
                race = Race.objects.get(name="elf")
                for i in range(2):
                    Skill.objects.create(
                        name=f'{player_temp[i]["name"]}',
                        bonus=f'{player_temp[i]["bonus"]}',
                        race=race
                    )
        except django.db.utils.IntegrityError:
            continue

    # Filling in the Guild table
    for player in players:
        try:
            if players[player]["guild"] is not None:
                Guild.objects.create(
                    name=f'{players[player]["guild"]["name"]}',
                    description=f'{players[player]["guild"]["description"]}'
                )
        except django.db.utils.IntegrityError:
            continue

    # Filling in the Player table
    global guild
    for player in players:
        if players[player]["guild"] is not None:
            guild = Guild.objects.get(
                name=f'{players[player]["guild"]["name"]}')
        race = Race.objects.get(name=f'{players[player]["race"]["name"]}')
        Player.objects.create(
            nickname=f'{player}',
            email=f'{players[player]["email"]}',
            bio=f'{players[player]["bio"]}',
            race=race,
            guild=guild if players[player]["guild"] is not None else None)


if __name__ == "__main__":
    main()
