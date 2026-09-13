import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        # 1. Обробка гільдії
        guild_data = data.get("guild")
        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description")}
            )

        # 2. Обробка раси (замінили data["race"] на data.get("race"))
        race_data = data.get("race")
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        # 3. Обробка навичок для цієї раси
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race_obj
                }
            )

        # 4. Створення самого гравця
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race_obj,
                "guild": guild_obj,
            }
        )
