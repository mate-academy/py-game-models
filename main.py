import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def load_file(file_path: str) -> dict | None:
    try:
        with open(file_path, "r") as source_file:
            return json.load(source_file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON from the file {file_path}.")
    return None


def get_or_create_race(race_data: dict) -> Race:
    return Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"]
    )[0]


def get_or_create_guild(guild_data: dict) -> Guild | None:
    if guild_data:
        return Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"]
        )[0]
    return None


def create_player(player_name: str, player_characteristics: dict) -> None:
    race_data = player_characteristics["race"]
    race = get_or_create_race(race_data)

    for skill in race_data["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )

    guild = get_or_create_guild(player_characteristics["guild"])

    Player.objects.get_or_create(
        nickname=player_name,
        email=player_characteristics["email"],
        bio=player_characteristics["bio"],
        race=race,
        guild=guild,
    )


def main() -> None:
    data = load_file("players.json")

    if data:
        for player_name, characteristics in data.items():
            create_player(player_name, characteristics)


if __name__ == "__main__":
    # Race.objects.all().delete()
    # Skill.objects.all().delete()
    # Player.objects.all().delete()
    # Guild.objects.all().delete()

    main()
