from typing import Optional

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def race_create(player_race_data: dict) -> Race:
    race_name = player_race_data["name"]
    race, created = Race.objects.get_or_create(
        name=race_name,
        description=player_race_data["description"]
    )
    if created:
        for skill_data in player_race_data["skills"]:
            Skill.objects.create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
    return race


def guild_create(guild_data: Optional[dict] = None) -> Guild | None:
    if guild_data is None:
        return
    guild_name = guild_data["name"]
    guild, created = Guild.objects.get_or_create(
        name=guild_name,
        description=guild_data["description"]
    )
    return guild


def main() -> None:
    with open("players.json") as conf:
        players = json.load(conf)
    for player, info in players.items():
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race_create(info["race"]),
            guild=guild_create(info["guild"]),
        )


if __name__ == "__main__":
    main()
