import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
from django.core.exceptions import ObjectDoesNotExist
from typing import Any, Dict


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
    with open("players.json") as data:
        players = json.load(data)

    for player, data in players.items():
        race_data = data.get("race")
        guild_data = data.get("guild")
        race = get_race(race_data)
        guild = get_guild(guild_data)
        Player.objects.create(
            nickname=player,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
