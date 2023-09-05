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

        player = Player.objects.create(
            nickname=player_name,
            email=data["email"],
            bio=data["bio"],
            race=race_obj,
            guild=guild_obj
        )
        player.save()


def get_or_create_skill(skill: dict, race_obj: Model) -> Union[Model, None]:
    if not skill:
        return None

    skill_name = skill["name"]
    if not Skill.objects.filter(name=skill_name).exists():
        skill_obj = Skill.objects.create(
            name=skill_name,
            bonus=skill["bonus"],
            race=race_obj
        )

    else:
        skill_obj = Skill.objects.get(name=skill_name)

    return skill_obj


def get_or_create_race(race_data: dict) -> Union[Model, None]:
    if not race_data:
        return None
    race_name = race_data["name"]
    if not Race.objects.filter(name=race_name).exists():
        race_obj = Race.objects.create(
            name=race_name,
            description=race_data["description"]
        )
    else:
        race_obj = Race.objects.get(name=race_name)

    return race_obj


def get_or_create_guild(guild_data: dict) -> Union[Model, None]:
    if not guild_data:
        return None

    guild_name = guild_data["name"]
    if not Guild.objects.filter(name=guild_name).exists():
        guild_obj = Guild.objects.create(
            name=guild_name,
            description=guild_data["description"])
    else:
        guild_obj = Guild.objects.get(name=guild_name)

    return guild_obj


if __name__ == "__main__":
    main()
