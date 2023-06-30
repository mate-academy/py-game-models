import json
from typing import List

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_player_race(race: dict[str]) -> None:
    if not Race.objects.filter(
        name=race["name"]
    ).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )


def create_player_guild(guild: dict[str]) -> None:
    if guild and not Guild.objects.filter(
        name=guild["name"]
    ).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )


def create_race_skills(skills: List[dict], race: str) -> None:
    for skill in skills:
        if not Skill.objects.filter(
            name=skill["name"]
        ).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=get_race_id(race)
            )


def get_guild_id(guild: dict[str]) -> int | None:
    if guild:
        return Guild.objects.get(name=guild["name"]).id


def get_race_id(race_name: str) -> int:
    return Race.objects.get(name=race_name).id


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        if Player.objects.filter(
            nickname=player_name
        ).exists():
            continue

        create_player_race(player_data["race"])
        create_player_guild(player_data["guild"])

        create_race_skills(
            player_data["race"]["skills"],
            player_data["race"]["name"]
        )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race_id=get_race_id(player_data["race"]["name"]),
            guild_id=get_guild_id(player_data["guild"])
        )


if __name__ == "__main__":
    main()
