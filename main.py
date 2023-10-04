import os
from json import load

import init_django_orm  # noqa: F401
from db.models import (
    Race, Skill, Player, Guild
)


def fill_game_tables(players: dict) -> None:
    for player_name, player_data in players.items():
        race = player_data["race"]
        race_name, skills = race["name"], race["skills"]

        Race.objects.get_or_create(name=race_name,
                                   description=race["description"])
        for skill in skills:
            current_race = Race.objects.get(name=f"{race_name}")
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=current_race)

        guild = player_data["guild"]
        if isinstance(guild, dict):
            Guild.objects.get_or_create(name=guild["name"],
                                        description=guild["description"])


def create_players(players: dict) -> None:
    for player_name, player_data in players.items():
        guild = player_data["guild"]
        if isinstance(guild, dict):
            guild = Guild.objects.get(name=guild["name"])
        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=player_data["race"]["name"]),
            guild=guild
        )


def main() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    players_path = os.path.join(current_dir, "players.json")
    with open(players_path) as players_data:
        players = load(players_data)
        fill_game_tables(players)
        create_players(players)


if __name__ == "__main__":
    main()

