import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        data_in_file = json.load(player_file)

    for player in data_in_file:
        race = data_in_file[player]["race"]
        guild = data_in_file[player]["guild"]
        guild_name = guild["name"] if guild else None
        guild_description = guild["description"] if guild else None

        obj_race, created_race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if guild is not None:
            obj_guild, created_guild = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        if guild is None:
            obj_guild = None

        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=obj_race
            )

        Player.objects.create(
            nickname=player,
            email=data_in_file[player]["email"],
            bio=data_in_file[player]["bio"],
            race=obj_race,
            guild=obj_guild
        )
