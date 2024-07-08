import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        data_in_file = json.load(player_file)
    for player in data_in_file:
        email = data_in_file[player]["email"]
        bio = data_in_file[player]["bio"]
        race = data_in_file[player]["race"]
        race_name = race["name"]
        race_description = race["description"]
        race_skills = race["skills"]
        guild = data_in_file[player]["guild"]
        guild_name = guild["name"]
        guild_description = guild["description"]
        break


if __name__ == "__main__":
    main()
