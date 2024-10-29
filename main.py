import json
from db.models import Race, Skill, Guild, Player
from typing import Any, Optional


def main() -> None:
    with open("players.json", "r") as file:
        players_data: dict[str, Any] = json.load(file)

    for player_name, player_data in players_data.items():
        if not isinstance(player_data, dict):
            continue

        race_data: Optional[dict[str, Any]] = player_data.get("race")
        if not isinstance(race_data, dict):
            continue

        guild_data: Optional[dict[str, Any]] = player_data.get("guild")
        if guild_data and not isinstance(guild_data, dict):
            guild_data = None

        skills_data: list[dict[str, str]] = race_data.get("skills", [])
        if not isinstance(skills_data, list):
            skills_data = []

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_data in skills_data:
            if isinstance(skill_data, dict):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"], race=race
                )

        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")},
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
            created_at=player_data.get("created_at"),
        )
