import json
import os

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def load_players_data(filename: str) -> dict:
    if not os.path.exists(filename):
        print(f"Error: The file {filename} does not exist.")
        return {}
    with open(filename, "r") as file:
        return json.load(file)


def create_race(data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=data["name"],
        defaults={"description": data.get("description", "")}
    )

    for skill_data in data.get("skills", []):
        Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={"bonus": skill_data["bonus"], "race": race}
        )
    return race


def create_guid(data: dict) -> Guild | None:
    if not data:
        return None

    guild, _ = Guild.objects.get_or_create(
        name=data["name"],
        defaults={"description": data.get("description", "")}
    )
    return guild


def create_players(player_name: str, player_data: dict) -> None:
    guild = create_guid(player_data["guild"])
    race = create_race(player_data["race"])

    player, created = Player.objects.update_or_create(
        nickname=player_name,
        defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild,
        }
    )
    if created:
        print(f"Created new player: {player.nickname}")
    else:
        print(f"Player {player.nickname} already exists.")


def main() -> None:
    players_data = load_players_data("players.json")
    for player_name, player_data in players_data.items():
        create_players(player_name, player_data)


if __name__ == "__main__":
    main()
