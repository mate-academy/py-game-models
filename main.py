import init_django_orm  # noqa: F401fr
import json

from pathlib import Path
from typing import Any, Dict
from db.models import Race, Skill, Player, Guild
from django.core.exceptions import ObjectDoesNotExist


def read_json() -> dict:
    path_to_file = Path(__file__).parent.joinpath("players.json")
    with open(path_to_file, "r") as file_read_stream:
        players = json.load(file_read_stream)

    return players


def create_race(race_info: Dict[str, Any]) -> Race:
    race = Race(
        name=race_info.get("name"),
        description=race_info.get("description")
    )
    race.save()

    for skill in race_info.get("skills"):
        Skill.objects.create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race
        )
    return race


def create_guild(guild_info: Dict[str, Any]) -> Guild:
    guild = Guild(
        name=guild_info.get("name"),
        description=guild_info.get("description")
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
    players = read_json()
    for player, info in players.items():
        race_info = info.get("race")
        guild_info = info.get("guild")
        race = get_race(race_info)
        guild = get_guild(guild_info)
        Player.objects.create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
