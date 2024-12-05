import json
from typing import Dict, Optional, List

from django.db import transaction

from db.models import Race, Skill, Guild, Player


def load_players_from_json(filename: str) -> Dict[str, dict]:
    with open(filename) as file:
        return json.load(file)


def create_or_update_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]}
    )
    return race


def create_or_update_skills(race: Race, skills_data: List[dict]) -> None:
    for skill_data in skills_data:
        Skill.objects.get_or_create(
            name=skill_data["name"], bonus=skill_data["bonus"], race=race
        )


def create_or_update_guild(guild_data: Optional[dict]) -> Optional[Guild]:
    if guild_data:
        guild, _ = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data.get("description")},
        )
        return guild
    return None


def create_player(
        player_name: str,
        player_data: dict,
        race: Race,
        guild: Optional[Guild]
) -> None:
    Player.objects.create(
        nickname=player_name,
        email=player_data["email"],
        bio=player_data["bio"],
        race=race,
        guild=guild,
    )


def main() -> None:
    data = load_players_from_json("players.json")

    with transaction.atomic():
        for player_name, player_data in data.items():
            race_data = player_data["race"]
            guild_data = player_data["guild"]

            race = create_or_update_race(race_data)
            create_or_update_skills(race, race_data["skills"])
            guild = create_or_update_guild(guild_data)

            create_player(player_name, player_data, race, guild)
