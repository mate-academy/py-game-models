import init_django_orm  # noqa: F401
import json
from typing import Optional

from db.models import Race, Skill, Player, Guild


def create_or_update_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"],
    )
    return race


def create_or_update_guild(guild_data: Optional[dict]) -> Optional[Guild]:
    if guild_data:
        guild, _ = Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"],
        )
        return guild
    return None


def create_or_update_skills(skills_data: list, race: Race) -> None:
    for skill in skills_data:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for user_name, user_info in data.items():
        race = create_or_update_race(user_info["race"])
        guild = create_or_update_guild(user_info["guild"])
        Player.objects.get_or_create(
            nickname=user_name,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild,
        )
        create_or_update_skills(user_info["race"]["skills"], race)


if __name__ == "__main__":
    main()
