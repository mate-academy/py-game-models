import json
from typing import Dict

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_or_create_race_and_skills(race: Dict) -> Race:
    player_race = Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )[0]
    if race["skills"]:
        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )
    return player_race


def get_or_create_guild(guild: Dict) -> Guild:
    return Guild.objects.get_or_create(
        name=guild["name"],
        description=guild["description"]
    )[0]


def main() -> None:
    with open("players.json", "r") as players_data:
        players = json.load(players_data)

    for player_nickname, player_info in players.items():
        player_race = get_or_create_race_and_skills(player_info["race"])

        player_guild = (
            get_or_create_guild(player_info["guild"])
            if player_info["guild"] else None
        )

        Player.objects.create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
