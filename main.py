import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_info = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info.get("description", "")}
        )

        for skill_info in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_info["name"],
                bonus=skill_info.get("bonus", ""),
                race=race
            )
        guild_info = player_data["guild"]
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info["description"]}
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild
            }
        )
