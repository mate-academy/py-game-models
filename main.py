# main.py
import json
import os

from db.models import Player, Race, Skill, Guild


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "db", "tests", "players.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    for nickname, details in data.items():
        email = details.get("email")
        bio = details.get("bio")

        race_data = details.get("race")
        if race_data is None:
            continue

        race_name = race_data.get("name")
        race_description = race_data.get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_data in race_data.get("skills", []):
            skill_name = skill_data.get("name")
            bonus = skill_data.get("bonus", "")

            skill, created = Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": bonus}
            )

            if not created and skill.race != race:
                skill.race = race
                skill.bonus = bonus
                skill.save()

        guild = None
        guild_data = details.get("guild")
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild,
            }
        )
