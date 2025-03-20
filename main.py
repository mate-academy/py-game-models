import os
import json
import django
from django.db import transaction
from typing import Dict, Any, Optional

# Настройка Django-окружения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from db.models import Race, Skill, Guild, Player


def main() -> None:
    """
    Основная функция для загрузки данных из players.json в базу данных.
    """
    # Открываем файл players.json и загружаем данные
    with open("players.json", "r", encoding="utf-8") as file:
        players_data: Dict[str, Any] = json.load(file)

    # Используем транзакцию для обеспечения атомарности операций
    with transaction.atomic():
        # Проходим по каждому игроку в данных
        for nickname, player_data in players_data.items():
            # Получаем данные о расе игрока
            race_data: Dict[str, Any] = player_data["race"]

            # Создаем или получаем расу
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            # Создаем или получаем навыки для расы
            for skill_data in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race}
                )

            # Получаем данные о гильдии игрока (если есть)
            guild_data: Optional[Dict[str, Any]] = player_data.get("guild")
            guild: Optional[Guild] = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            # Создаем или получаем игрока
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
