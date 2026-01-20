from __future__ import annotations

import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def read_players_file(file_path: str) -> dict | None:
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
    return None


def main() -> None:

    players = read_players_file("players.json")

    for user in players:

        user_info = players[user]
        race_info = user_info["race"]
        skills_info = race_info["skills"]
        guild_info = user_info["guild"]

        race, created = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        if skills_info:
            for skill in skills_info:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        guild = None
        if guild_info:
            guild, created = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        Player.objects.create(
            nickname=user,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
