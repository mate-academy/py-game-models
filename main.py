import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    global guild_name

    Player.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json") as player_data:
        players = json.load(player_data)

    for player in players:
        nickname = player
        email = players[player]["email"]
        bio = players[player]["bio"]
        race_data = players[player]["race"]
        guild_data = players[player]["guild"]

        if not Race.objects.filter(name=race_data["name"]).exists():
            Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )

        race_name = Race.objects.get(name=race_data["name"])

        for skill in race_data["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_name
                )

        if guild_data:
            if not Guild.objects.filter(name=guild_data["name"]).exists():
                Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
                guild_name = Guild.objects.get(name=guild_data["name"])
        else:
            guild_name = None

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(nickname=nickname,
                                  email=email,
                                  bio=bio,
                                  race=race_name,
                                  guild=guild_name)


if __name__ == "__main__":
    main()
