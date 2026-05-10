import json
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from db.models import Guild, Player, Race, Skill  # noqa: E402


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, data in players_data.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                }
            )

        guild = None
        if data.get("guild"):
            guild_data = data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )
