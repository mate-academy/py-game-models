import json
from typing import Union
from django.db.models import Model

import init_django_orm  # noqa: F401

from db.models import Guild, Player, Skill, Race


def main() -> None:
    with open("players.json", "r") as file_pointer:
        data = json.load(file_pointer)

    for player_name, data in data.items():
        guild_data = data.get("guild")
        race_data = data.get("race")

        guild_obj = get_or_create_guild(guild_data)
        race_obj = get_or_create_race(race_data)

        for skill in race_data["skills"]:
            get_or_create_skill(skill, race_obj)

        Player.objects.get_or_create(
            nickname=player_name,
            email=data["email"],
            bio=data["bio"],
            race=race_obj,
            guild=guild_obj
        )


def get_or_create_skill(skill: dict, race_obj: Model) -> Union[Model, None]:
    if not skill:
        return None

    skill_obj, created = Skill.objects.get_or_create(
        name=skill["name"],
        bonus=skill["bonus"],
        race=race_obj
    )

    return skill_obj


def get_or_create_race(race_data: dict) -> Union[Model, None]:
    if not race_data:
        return None

    race_obj, created = Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"]
    )

    return race_obj


def get_or_create_guild(guild_data: dict) -> Union[Model, None]:
    if not guild_data:
        return None

    guild_obj, created = Guild.objects.get_or_create(
        name=guild_data["name"],
        description=guild_data["description"]
    )

    return guild_obj


if __name__ == "__main__":
    main()
