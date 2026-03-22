import json
from pathlib import Path

from django.core.management import call_command

from db.models import Guild, Player, Race, Skill


def main() -> None:
    call_command("migrate", verbosity=0)

    file_path = Path("players.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")

        if not race_data:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description", "")
            },
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race,
                },
            )

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            },
        )
