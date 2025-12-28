from __future__ import annotations
import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_guild(guild_dict: dict | None) -> Guild | None:
    if guild_dict:
        guild, created = Guild.objects.get_or_create(
            **guild_dict
        )
        return guild

    return None


def get_race(race_dict: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_dict["name"],
        description=race_dict["description"]
    )

    for skill in race_dict["skills"]:
        Skill.objects.get_or_create(
            **skill,
            race=race
        )

    return race


def main() -> None:
    with open("players.json") as players_data:
        players_info = json.load(players_data)

    for nickname, player_info in players_info.items():
        Player.objects.get_or_create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            guild=get_guild(player_info["guild"]),
            race=get_race(player_info["race"])
        )


if __name__ == "__main__":
    main()
