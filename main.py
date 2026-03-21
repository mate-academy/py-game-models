import django
import json
import os
from db.models import Race, Skill, Guild, Player


def main() -> None:
    django.setup()

    json_path = os.path.join(os.path.dirname(__file__), "players.json")
    if not os.path.exists(json_path):
        return

    with open(json_path, "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for data in players_data:
        # Пропускаем элементы, которые не являются словарями
        if not isinstance(data, dict):
            continue

        # Гильдия
        guild_name = data.get("guild")
        guild = None
        if guild_name:
            guild, _ = Guild.objects.get_or_create(name=guild_name)

        # Раса
        race_data = data["race"]
        # Если раса — строка, создаём расу с пустым описанием
        if isinstance(race_data, str):
            race, _ = Race.objects.get_or_create(
                name=race_data,
                defaults={"description": ""}
            )
        else:
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )
            # Навыки
            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data.get("bonus", "")}
                )

        # Игрок
        Player.objects.get_or_create(
            nickname=data["nickname"],
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild,
            }
        )
