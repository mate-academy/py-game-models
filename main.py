import init_django_orm  # noqa: F401
import json
from typing import Dict, Any

from django.core.exceptions import ObjectDoesNotExist
from db.models import Race, Skill, Player, Guild


def get_python_data_from_json(json_file_path: str) -> Dict[str, Any]:
    with open(json_file_path) as json_data:
        data = json.load(json_data)
        return data


def create_race(data: Dict[str, Any]) -> Race:
    race = Race(
        name=data.get("name"),
        description=data.get("description"),
    )
    race.save()
    for skill in data.get("skills"):
        Skill.objects.create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race,
        )
    return race


def create_guild(data: Dict[str, Any]) -> Guild:
    guild = Guild(
        name=data.get("name"),
        description=data.get("description"),
    )
    guild.save()
    return guild


def get_race(data: Dict[str, Any]) -> Race:
    try:
        race = Race.objects.get(name=data.get("name"))
    except ObjectDoesNotExist:
        race = create_race(data)
    return race


def get_guild(data: Dict[str, Any]) -> Guild:
    guild = None
    if data:
        try:
            guild = Guild.objects.get(name=data.get("name"))
        except ObjectDoesNotExist:
            guild = create_guild(data)
    return guild


def main() -> None:

    data = get_python_data_from_json("players.json")
    for player, data in data.items():
        race = get_race(data.get("race"))
        guild = get_guild(data.get("guild"))
        Player.objects.create(
            nickname=player,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
