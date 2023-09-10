import json
from typing import Union

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def analyse_race(input_race: dict) -> Race:
    """Function analyse if race exists, adding new or returning existing"""
    unique_name = input_race["name"]
    if Race.objects.filter(name=unique_name).exists():
        return Race.objects.get(name=unique_name)
    return Race.objects.create(
        name=unique_name,
        description=input_race["description"]
    )


def analyse_skills(input_skills: dict, input_race: Race) -> list:
    """Function add new skills in DB and return list of skills instances"""
    skills_set = []
    for skill in input_skills:
        unique_name = skill["name"]
        if Skill.objects.filter(name=unique_name):
            skills_set.append(Skill.objects.get(name=unique_name))
        else:
            skills_set.append(
                Skill.objects.create(
                    name=unique_name,
                    bonus=skill["bonus"],
                    race=input_race
                )
            )
    return skills_set


def analyse_guild(input_guild: dict) -> Union[Race | None]:
    """Function analyse if guild exists, adding new or returning existing"""
    if input_guild is None:
        return
    unique_name = input_guild["name"]
    if Guild.objects.filter(name=unique_name).exists():
        return Guild.objects.get(name=unique_name)
    return Guild.objects.create(
        name=unique_name,
        description=input_guild["description"]
    )


def main() -> None:
    with open("players.json", "r") as f:
        users = json.load(f)
    for username in users:
        user_data = users[username]
        race = analyse_race(user_data["race"])
        analyse_skills(user_data["race"]["skills"], race)
        guild = analyse_guild(user_data["guild"])
        Player.objects.create(
            nickname=username,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
