import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        content = json.load(file)

    for key, value in content.items():
        guild = None
        guild_data = value.get("guild")
        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"],
                },
            )

        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={
                "description": value["race"]["description"],
            },
        )

        for skill_data in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race},
            )

        Player.objects.get_or_create(
            nickname=key,
            defaults={
                "email": value["email"],
                "bio": value["bio"],
                "race": race,
                "guild": guild,
            },
        )
