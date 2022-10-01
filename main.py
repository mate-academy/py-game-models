import django.db

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main():
    with open("players.json", "r") as file_json:
        players = json.load(file_json)
    for player in players:
        # Race
        try:
            rc = Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]
            )
        except django.db.IntegrityError:
            rc = Race.objects.get(name=players[player]["race"]["name"])
        # Guild
        if players[player]["guild"] is None:
            gld = None
        else:
            try:
                gld = Guild.objects.create(
                    name=players[player]["guild"]["name"],
                    description=players[player]["guild"]["description"]
                )
            except django.db.IntegrityError:
                gld = Guild.objects.get(name=players[player]["guild"]["name"])
        # Skill
        for skill in players[player]["race"]["skills"]:
            try:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=rc
                )
            except django.db.IntegrityError:
                Skill.objects.get(name=skill["name"])
        # Player
        try:
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=rc,
                guild=gld
            )
        except django.db.IntegrityError:
            Player.objects.get(nickname=player)


if __name__ == "__main__":
    main()
