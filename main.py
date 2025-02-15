from sqlite3 import IntegrityError

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    # Load data from .json
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Iterating over data
    for player_name, player_data in data.items():
        race = player_data["race"]
        skills = race["skills"]
        guild_data = player_data.get("guild")

        # CHECK IF RACE EXIST, IF NOT CREATE
        try:
            Race.objects.get_or_create(name=race["name"],
                                       description=race["description"])
        except IntegrityError as e:
            print(f"IntegrityError: {e}"
                  f" - Skipping race creation for {race["name"]}")

        # CHECK IF SKILLS EXIST, IF NOT CREATE AND INSERT WITH RACES KEYS
        for skill in skills:
            try:
                Skill.objects.get_or_create(name=skill["name"],
                                            defaults={"bonus": skill["bonus"],
                                            "race": Race.objects.get(
                                                name=race["name"])})
            except IntegrityError as e:
                print(f"IntegrityError: {e}"
                      f" - Skipping skill creation for {skill["name"]}")

        # CHECK IF GUILD EXIST, IF NOT CREATE
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")})

        # CREATING PLAYER WITH FULL DATA
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": Race.objects.get(name=race["name"]),
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
