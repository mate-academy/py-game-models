import json
from pathlib import Path
from django.utils import timezone
from db.models import Player, Race, Skill, Guild

import init_django_orm  # noqa: F401


def main() -> None:
    file_path = Path(__file__).parent / "players.json"

    with open(file_path, "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

    for skill_data in race_data["skills"]:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            race=race,
            defaults={"bonus": skill_data["bonus"]}
        )

    guild_data = player_data.get("guild")
    guild = None
    if guild_data:
        guild, _ = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={
                "description": guild_data.get("description")
            }
        )

    Player.objects.get_or_create(
        nickname=nickname,
        defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild,
            "created_at": timezone.now()
        }
    )


if __name__ == "__main__":
    main()
