import init_django_orm  # noqa: F401
import json
from typing import Dict, Any

from django.core.exceptions import ObjectDoesNotExist
from db.models import Race, Skill, Player, Guild


def get_python_data_from_json(json_file_path: str) -> Dict[str, Any]:
    with open(json_file_path) as json_data:
        data = json.load(json_data)
        return data


def get_race(data: Dict[str, Any]) -> Race:
    race, created = Race.objects.get_or_create(
        name=data.get("name"),
        defaults={
            "description": data.get("description"),
        }
    )
    if created:
        for skill in data.get("skills"):
            Skill.objects.create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race,
            )
    return race


def get_guild(data: Dict[str, Any]) -> Guild:
    guild = None
    if data and data.get("name"):
        try:
            guild, created = Guild.objects.get_or_create(
                name=data.get("name"),
                defaults={
                    "description": data.get("description"),
                }
            )
        except ObjectDoesNotExist:
            pass
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
