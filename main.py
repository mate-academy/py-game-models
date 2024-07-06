import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def load_players(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def main() -> None:
    path_to_file = "players.json"
    data_players = load_players(path_to_file)

    for key, value in data_players.items():
        print(f"key: {key}")

        data_race = value["race"]
        get_race, created = Race.objects.get_or_create(
            name=data_race["name"],
            description=data_race["description"]
        )

        for skill in data_race["skills"]:
            Skill.objects.skill_set.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=get_race
            )

        get_guild = None
        if value["guild"]:
            data_guild = value["guild"]
            get_guild, created = Guild.objects.get_or_create(
                name=data_guild["name"],
                description=data_guild["description"]
            )

        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=get_race,
            guild=get_guild
        )


if __name__ == "__main__":
    main()
