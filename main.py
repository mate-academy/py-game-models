import json
from typing import Optional

import init_django_orm  # noqa: F401
from django.db import IntegrityError

from db.models import Race, Skill, Player, Guild


def load_data(filepath: str) -> dict:
    with open(filepath) as file:
        return json.load(file)


def create_or_get_guild(guild_data: dict) -> Optional[Guild]:
    if guild_data:
        guild, _ = Guild.objects.get_or_create(
            name=guild_data.get("name"),
            defaults={"description": guild_data.get("description", "")}
        )
        return guild
    return None


def create_skills(
        race: Race,
        skills_data: list
) -> None:
    for skill_data in skills_data:
        Skill.objects.get_or_create(
            name=skill_data.get("name"),
            bonus=skill_data.get("bonus"),
            race=race
        )


def create_player(
        nickname: str,
        player_data: dict
) -> None:
    race_data = player_data.get("race")
    guild_data = player_data.get("guild")

    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description", "")}
    )

    guild = create_or_get_guild(guild_data) if guild_data else None

    create_skills(race, race_data.get("skills", []))

    try:
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )
    except IntegrityError:
        print(f"Player with nickname {nickname} already exists.")


def main() -> None:
    data = load_data("players.json")
    for nickname, player_data in data.items():
        create_player(nickname, player_data)


if __name__ == "__main__":
    main()
