import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race_name = player_info["race"]["name"]
        race_description = player_info["race"]["description"]
        race, created_race = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        guild_name = (player_info["guild"]["name"]
                      if player_info["guild"] else None)
        guild = None
        if guild_name is not None:
            guild_description = player_info["guild"]["description"]
            guild, created_guild = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        skills = player_info["race"]["skills"]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        email = player_info["email"]
        bio = player_info["bio"]
        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
