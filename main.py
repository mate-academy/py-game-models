import json
from pathlib import Path
from django.db import transaction
from db.models import Player, Race, Skill, Guild

def main():
    file_path = Path(__file__).resolve().parent / "players.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for player_name, details in data.items():
        with transaction.atomic():
            
            race, _ = Race.objects.get_or_create(
                name=details["race"]["name"],
                defaults={"description": details["race"]["description"]}
            )

            
            for skill_data in details["race"]["skills"]:
                skill, created = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={
                        "bonus": skill_data["bonus"],
                        "race": race
                    }
                )
                
                if not created and skill.race != race:
                    skill.race = race
                    skill.save()

            
            guild_data = details.get("guild")
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data["description"]}
                )

            
            Player.objects.get_or_create(
                email=details["email"],
                defaults={
                    "name": player_name,
                    "bio": details["bio"],
                    "race": race,
                    "guild": guild
                }
            )