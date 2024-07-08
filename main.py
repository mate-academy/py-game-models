import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json", "r") as player_file:
        data_in_file = json.load(player_file)

    for player in data_in_file:
        email = data_in_file[player]["email"]
        bio = data_in_file[player]["bio"]
        race = data_in_file[player]["race"]
        race_name = race["name"]
        race_description = race["description"]
        race_skills = race["skills"]
        guild = data_in_file[player]["guild"]
        guild_name = guild["name"] if guild else None
        guild_description = guild["description"] if guild else None

        obj_race, created_race = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        if guild is not None:
            obj_guild, created_guild = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        for skill in race_skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=obj_race
            )

        Player.objects.create(
            nickname=player,
            email=email,
            bio=bio,
            race=obj_race,
            guild=obj_guild
        )
