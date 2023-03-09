from __future__ import annotations

import json
from typing import Dict

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race_info: Dict[str]) -> Race:
    return Race.objects.get_or_create(
        name=race_info["name"],
        defaults={"description": race_info.get("description")},
    )[0]


def create_skill(race: Race, skill_info: Dict[str]) -> Skill:
    return Skill.objects.get_or_create(
        name=skill_info["name"],
        defaults={"bonus": skill_info.get("bonus"), "race": race},
    )[0]


def create_guild(guild_info: Dict[str]) -> Guild:
    return Guild.objects.get_or_create(
        name=guild_info["name"],
        defaults={"description": guild_info.get("description")},
    )[0]


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        player_race_info = player_info.get("race")

        if player_race_info:
            race = create_race(player_race_info)
            player_skills_info = player_race_info.get("skills")

            if player_skills_info:
                for skill in player_skills_info:
                    create_skill(race, skill)

        guild = None
        player_guild_info = player_info.get("guild")

        if player_guild_info:
            guild = create_guild(player_guild_info)

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
