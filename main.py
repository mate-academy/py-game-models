import init_django_orm  # noqa: F401
import json

from django.db import transaction
from typing import List
from db.models import Race, Skill, Player, Guild


def load_players_data(file_path: str) -> dict:
    with open(file_path) as file:
        players_data = json.load(file)
    return players_data


def create_race(race_data: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data.get("description")},
    )
    return race


def create_guild(guild_data: dict) -> Guild:
    if guild_data:
        guild, created = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data.get("description")},
        )
    else:
        guild = None
    return guild


def create_skills(race_data: dict, race: Race) -> List[Skill]:
    for skill_data in race_data["skills"]:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race
        )


def create_player(player_data: dict) -> Player:
    race_data = player_data["race"]
    race = create_race(race_data)

    guild_data = player_data["guild"]
    guild = create_guild(guild_data)

    create_skills(race_data, race)

    player, created = Player.objects.get_or_create(
        nickname=player_data["nickname"],
        defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild,
        },
    )
    return player


@transaction.atomic
def main() -> None:
    players_data = load_players_data("players.json")

    for player_name, player_data in players_data.items():
        player_data["nickname"] = player_name
        create_player(player_data)


if __name__ == "__main__":
    main()
