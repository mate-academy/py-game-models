# main.py
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from db.models import Guild, Player, Race, Skill


def _load_players() -> List[Dict[str, Any]]:
    path = Path(__file__).resolve().parent / "players.json"
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data["players"] if isinstance(data, dict) else data


def main() -> None:
    players = _load_players()

    for player in players:
        race_data = player["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

        guild_data = player.get("guild")
        guild: Optional[Guild] = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        Player.objects.get_or_create(
            nickname=player["nickname"],
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race": race,
                "guild": guild,
            },
        )
