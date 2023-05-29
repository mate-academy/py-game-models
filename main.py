from typing import Optional

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def race_create(player_race_data: dict) -> Race:
    race_name = player_race_data.get("name")
    race, created = Race.objects.get_or_create(
        name=race_name,
        description=player_race_data.get("description")
    )
    if created:
        for skill_data in player_race_data.get("skills"):
            Skill.objects.create(
                name=skill_data.get("name"),
                bonus=skill_data.get("bonus"),
                race=race
            )
    return race


def guild_create(guild_data: Optional[dict] = None) -> Guild | None:
    if guild_data is None:
        return
    guild_name = guild_data.get("name")
    guild, _ = Guild.objects.get_or_create(
        name=guild_name,
        description=guild_data.get("description")
    )
    return guild


def main() -> None:
    with open("players.json") as conf:
        players = json.load(conf)
    for player, info in players.items():
        Player.objects.create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_create(info.get("race")),
            guild=guild_create(info.get("guild")),
        )


if __name__ == "__main__":
    main()
