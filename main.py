import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)
        for nickname, value in players_data.items():
            email = value["email"]
            bio = value["bio"]
            if value["guild"]:
                guild_name = value["guild"]["name"]
                guild_description = value["guild"]["description"]

            print(nickname,email, bio, guild_name, guild_description)
            print()
            for race in value["race"]:
                race_name = race["name"]
                race_description = race["description"]

                for skill in race["skills"]:
                    skill_name = skill["name"]
                    skill_bonus = skill["bonus"]



if __name__ == "__main__":
    main()
