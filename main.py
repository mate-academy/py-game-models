import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for key, value in players.items():
        race_name = value["race"]["name"]
        race_description = value["race"]["description"]
        race, created_race = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        guild_name = (value["guild"]["name"]
                      if value["guild"] else None)
        guild = None
        if guild_name is not None:
            guild_description = value["guild"]["description"]
            guild, created_guild = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        skills = value["race"]["skills"]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        email = value["email"]
        bio = value["bio"]
        Player.objects.create(
            nickname=key,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )
