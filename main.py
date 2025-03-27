import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for player_nickname, player_info in players_data.items():

        guild = player_info["guild"]
        guild_obj = None

        if guild:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        race = player_info["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if race["skills"]:
            for skill in race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

        Player.objects.create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
