import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for name in data:
        user_data = data[name]
        race_data = user_data["race"]
        guild_data = user_data.get("guild")

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"]
            }
        )

        for skill_data in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description")
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": user_data["email"],
                "bio": user_data["bio"],
                "race": race,
                "guild": guild
            }
        )
