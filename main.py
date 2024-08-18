import os
import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = "players.json"


def read_file(file_name: str) -> dict:
    try:
        with open(os.path.join(BASE_DIR, file_name), "r") as file:
            file_input = json.load(file)
    except FileNotFoundError as e:
        print(f"Couldn't find a {file_name} file: {e}")
    else:
        return file_input


def clear_db() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()


def main() -> None:
    players_info = read_file(FILE_NAME)
    clear_db()

    for player, data in players_info.items():

        player_race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"],
        )[0]

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )

        player_guild = None
        if data["guild"] is not None:
            player_guild = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )[0]

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
