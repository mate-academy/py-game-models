import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race_info = player_info["race"]
        if race_info:
            race_info, race_created = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        guild_info = player_info["guild"]
        if guild_info:
            guild_info, guild_created = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        skills_info = player_info["race"]["skills"]
        if skills_info:
            for skill in skills_info:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_info
                )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_info,
            guild=guild_info
        )


if __name__ == "__main__":
    main()
