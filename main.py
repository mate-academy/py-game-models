from django.core.exceptions import ObjectDoesNotExist

import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def get_or_create_race(data):
    try:
        race = Race.objects.get(name=data["name"])
    except ObjectDoesNotExist:
        race = Race.objects.create(name=data["name"], description=data["description"])
    return race


def get_or_create_skill(data, race):
    try:
        skill = Skill.objects.get(name=data["name"])
    except ObjectDoesNotExist:
        skill = Skill.objects.create(name=data["name"], bonus=data["bonus"], race=race)
    return skill


def get_or_create_guild(data):
    try:
        guild = Guild.objects.get(name=data["name"])
    except ObjectDoesNotExist:
        guild = Guild.objects.create(name=data["name"], description=data["description"])
    return guild


def main() -> None:
    with open("players.json") as config_file:
        data = json.load(config_file)
        for player in data.values():
            race = get_or_create_race(player["race"])
            for skill in player["race"]["skills"]:
                get_or_create_skill(skill, race)

            guild = get_or_create_guild(player["guild"]) if player["guild"] else None

            Player.objects.create(
                nickname=player["email"].split("@")[0],
                email=player["email"],
                bio=player["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
