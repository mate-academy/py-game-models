import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as data_source:
        players = json.load(data_source)

    for player in players:
        player_info = players[player]
        player_race_info = player_info["race"]
        if not Race.objects.filter(name=player_info["race"]["name"]).exists():
            Race.objects.create(
                name=player_race_info["name"],
                description=player_race_info["description"]
            )

        player_race = Race.objects.get(name=player_info["race"]["name"])
        for skill in player_race_info["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        player_guild_info = player_info["guild"]
        if player_guild_info:
            if not Guild.objects.filter(name=player_guild_info["name"]):
                Guild.objects.create(
                    name=player_guild_info["name"],
                    description=player_guild_info["description"]
                )
            player_guild = Guild.objects.get(name=player_guild_info["name"])
        else:
            player_guild = None

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
