import json
from typing import Dict, Any, Optional, Tuple, Type
from django.db import transaction


# Импортируем функцию для настройки Django
from setup_django import setup_django


def get_models() -> Tuple[
    Type["Race"],  # noqa: F821
    Type["Skill"],  # noqa: F821
    Type["Guild"],  # noqa: F821
    Type["Player"],  # noqa: F821
]:
    """
    Ленивая загрузка моделей Django.

    Returns:
        Кортеж с моделями Race, Skill, Guild, Player.
    """
    # Настройка Django перед импортом моделей
    setup_django()

    # Импортируем модели после настройки Django
    from db.models import Race, Skill, Guild, Player
    return Race, Skill, Guild, Player


def main() -> None:
    """
    Основная функция для загрузки
    данных из players.json в базу данных.
    """
    # Ленивая загрузка моделей
    race_model, skill_model, guild_model, player_model = get_models()

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
            race, _ = race_model.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            # Создаем или получаем навыки для расы
            for skill_data in race_data["skills"]:
                skill_model.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race}
                )

            # Получаем данные о гильдии игрока (если есть)
            guild_data: Optional[Dict[str, Any]] = player_data.get("guild")
            guild: Optional[guild_model] = None
            if guild_data:
                guild, _ = guild_model.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            # Создаем или получаем игрока
            player_model.objects.get_or_create(
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
