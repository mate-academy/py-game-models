from __future__ import annotations

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
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


def create_race(data: dict) -> Race:
    if not Race.objects.filter(name=data["race"]["name"]).exists():
        return Race.objects.create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
    return Race.objects.get(name=data["race"]["name"])


def create_skills(data: dict) -> None:
    for skill in data["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=create_race(data)
            )


def create_guild(data: dict) -> Guild | None:
    if data["guild"]:
        if not Guild.objects.filter(name=data["guild"]["name"]).exists():
            return Guild.objects.create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )
        return Guild.objects.get(name=data["guild"]["name"])

    return None


if __name__ == "__main__":
    main()
