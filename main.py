import os
import django
import json
from datetime import datetime
from db.models import Player, Guild, Race, Skill

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for player_name, player_data in players_data.items():
        race_data = player_data["race"]
        if player_data["guild"]:
            guild_data = player_data["guild"]
        race_instance, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
        guild_instance, _ = Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"]
            if guild_data["description"]
            else None
        )
        if "skills" in race_data:
            skills_data = player_data["race"]["skills"]
            for skill_data in skills_data:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race_instance
                )
        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_instance,
            guild=guild_instance if player_data["guild"] else None,
            defaults={"created_at": datetime.now()}
        )
