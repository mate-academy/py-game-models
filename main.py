import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Guild, Player, Race, Skill


def main() -> None:
    players_path = Path(__file__).resolve().parent / "players.json"
    with players_path.open(encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        race_info = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")},
        )

        for skill_info in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={
                    "bonus": skill_info["bonus"],
                    "race": race,
                },
            )

        guild = None
        guild_info = player_info.get("guild")
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
