import init_django_orm  # noqa: F401fr
import json

from pathlib import Path
from typing import Any, Dict
from db.models import Race, Skill, Player, Guild


def read_json() -> dict:
    path_to_file = Path(__file__).parent.joinpath("players.json")
    with open(path_to_file, "r") as file_read_stream:
        players = json.load(file_read_stream)

    return players


def get_or_create_race(data: Dict[str, Any]) -> Race:
    if data:
        obj_race, created_race = Race.objects.get_or_create(
            name=data.get("name"),
            description=data.get("description")
        )

        for skill in data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=obj_race
            )

        return obj_race


def get_or_create_guild(data: Dict[str, Any]) -> Guild:
    if data:
        obj_guild, created_guild = Guild.objects.get_or_create(
            name=data.get("name"),
            description=data.get("description")
        )

        return obj_guild


def main() -> None:
    players = read_json()
    for player, info in players.items():
        race_info = info.get("race")
        guild_info = info.get("guild")
        race = get_or_create_race(race_info)
        guild = get_or_create_guild(guild_info)
        Player.objects.create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
