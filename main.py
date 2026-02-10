# main.py
import json
from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")
        if not race_data:
            continue  # Skip if no race data

        race_name = race_data.get("name")
        if not race_name:
            continue  # Skip if no race name

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_data.get("description", "")}
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill_name = skill_data.get("name")
            if not skill_name:
                continue  # Skip if no skill name

            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race
                }
            )

        email = player_data.get("email")
        if not email:
            continue  # Skip if no email

        bio = player_data.get("bio", "")  # Default to empty if missing

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_data.get("description")}
                )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )
