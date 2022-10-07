import json
from typing import Union

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_nickname, player_data in data.items():
        race = create_race(player_data)
        guild = create_guild(player_data)
        create_skills(player_data)

        Player.objects.create(
            nickname=player_nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


def create_race(player_data: dict) -> Race:
    if not Race.objects.filter(name=player_data["race"]["name"]).exists():
        return Race.objects.create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
    return Race.objects.get(name=player_data["race"]["name"])


def create_skills(player_data: dict) -> None:
    for skill in player_data["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=create_race(player_data)
            )


def create_guild(player_data: dict) -> Union[Guild, None]:
    if player_data["guild"]:
        if not Guild.objects.filter(
                name=player_data["guild"]["name"]
        ).exists():
            return Guild.objects.create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )
        return Guild.objects.get(name=player_data["guild"]["name"])
    return None


if __name__ == "__main__":
    main()
