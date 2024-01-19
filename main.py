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
        nickname = player_name
        email = player_data["email"]
        bio = player_data["bio"]
        race_data = player_data["race"]
        race_name = race_data["name"]
        race_description = race_data["description"]
        if player_data["guild"]:
            guild_data = player_data["guild"]
            guild_name = guild_data["name"]
            guild_description = guild_data["description"] \
                if guild_data["description"]\
                else None
        race_instance, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        guild_instance, _ = Guild.objects.get_or_create(
            name=guild_name,
            description=guild_description
        )
        if "skills" in race_data:
            skills_data = race_data["skills"]
            for skill_data in skills_data:
                skill_name = skill_data["name"]
                skill_bonus = skill_data["bonus"]
                skill, _ = Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_instance
                )
        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_instance,
            guild=guild_instance if player_data["guild"] else None,
            defaults={"created_at": datetime.now()}
        )
