import json
import os
from typing import Optional

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def load_players(file_path: str) -> dict:
    file_path = os.path.abspath(file_path)
    with open(file_path, "r") as file:
        return json.load(file)


def race(info: dict) -> Optional[Race]:
    race_obj, _ = Race.objects.get_or_create(
        name=info["race"]["name"],
        description=info["race"]["description"]
        if info["race"]["description"] else None,
    ) if info["race"] else None

    return race_obj


def skill(info: dict) -> None:
    for skill in info["race"]["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race(info)
        )


def guild(info: dict) -> Optional[Guild]:
    guild_obj = None
    if info["guild"]:
        guild_obj, _ = Guild.objects.get_or_create(
            name=info["guild"]["name"],
            description=info["guild"]["description"]
            if info["guild"]["description"] else None,
        )

    return guild_obj


def main() -> None:
    players = load_players("players.json")

    for nickname, info in players.items():
        email = info["email"]
        bio = info["bio"]
        race_for_person = race(info)

        skill(info)

        guild_for_person = guild(info)

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_for_person,
            guild=guild_for_person,
        )


if __name__ == "__main__":
    main()
