import json
import os
from typing import Optional

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def load_players(file_path: str) -> dict:
    file_path = os.path.abspath(file_path)
    with open(file_path, "r") as file:
        return json.load(file)


def race(players: dict, person: str) -> Optional[Race]:
    race_obj, _ = Race.objects.get_or_create(
        name=players[person]["race"]["name"],
        description=players[person]["race"]["description"]
        if players[person]["race"]["description"] else None,
    ) if players[person]["race"] else None

    return race_obj


def skill(players: dict, person: str) -> None:
    for skill in players[person]["race"]["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race(players, person)
        )


def guild(players: dict, person: str) -> Optional[Guild]:
    guild_obj = None
    if players[person]["guild"]:
        guild_obj, _ = Guild.objects.get_or_create(
            name=players[person]["guild"]["name"],
            description=players[person]["guild"]["description"]
            if players[person]["guild"]["description"] else None,
        )

    return guild_obj


def main() -> None:
    players = load_players("players.json")

    for nickname, info in players.items():
        email = info["email"]
        bio = info["bio"]
        race_for_person = race(players, nickname)

        skill(players, nickname)

        guild_for_person = guild(players, nickname)

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_for_person,
            guild=guild_for_person,
        )


if __name__ == "__main__":
    main()
