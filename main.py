import json

import init_django_orm  # noqa: F401
from django.db.models import QuerySet

from db.models import Race, Skill, Guild, Player


def main() -> QuerySet:
    with open("players.json", "r", encoding="utf-8") as file_name:
        players_data = json.load(file_name)
    for nickname, data in players_data.items():
        race_data = data.get("race")
        if race_data is None:
            continue

        race_name = race_data.get("name")
        race_description = race_data.get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description},
        )

        for race_obj in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=race_obj["name"],
                defaults={"bonus": race_obj.get("bonus", ""), "race": race},
            )

        guild_obj = None
        guild_data = data.get("guild")
        if guild_data is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild_obj,
            },
        )

    return Player.objects.all()
