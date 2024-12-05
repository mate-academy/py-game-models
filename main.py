import json
from typing import List

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def create_races(data_values: List[dict]) -> None:
    for user_data in data_values:
        Race.objects.get_or_create(
            name=user_data["race"]["name"],
            description=user_data["race"]["description"]
        )


def create_skills(data_values: List[dict]) -> None:
    for user_data in data_values:
        race = Race.objects.get(
            name=user_data["race"]["name"]
        )
        for skill in user_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def create_guilds(data_values: List[dict]) -> None:
    for user_data in data_values:
        if user_data["guild"]:
            guild_data = user_data.get("guild")
            Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description", None)
            )


def create_players(data: dict) -> None:
    for user, user_data in data.items():
        race = Race.objects.get(
            name=user_data["race"]["name"]
        )
        guild = None
        if user_data["guild"]:
            guild = Guild.objects.get(
                name=user_data.get("guild")
                .get("name")
            )
        Player.objects.create(
            nickname=user,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild
        )


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    create_races(data.values())
    create_skills(data.values())
    create_guilds(data.values())
    create_players(data)


if __name__ == "__main__":
    main()
