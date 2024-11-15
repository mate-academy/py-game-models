import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    if not players_data:
        print("Файл JSON порожній або має неправильну структуру.")
        return

    for player in players_data.values():
        # Створення/отримання раси
        race_data = player.get("race", {})
        race_name = race_data.get("name")
        race_desc = race_data.get("description", "")
        race, created = Race.objects.get_or_create(name=race_name, defaults={"description": race_desc})

        # Створення навичок для раси
        skills_data = race_data.get("skills", [])
        for skill in skills_data:
            # Оновлений виклик get_or_create для Skills з додаванням race
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race  # Встановлюємо зв'язок з race
            )

        # Створення/отримання гільдії
        guild_data = player.get("guild", {})
        guild_name = guild_data.get("name")
        guild_desc = guild_data.get("description", "")  # Якщо опис гільдії відсутній, встановлюємо порожнє значення
        guild, created = Guild.objects.get_or_create(name=guild_name, defaults={"description": guild_desc})

        # Створення/оновлення гравця
        Player.objects.get_or_create(
            nickname=player["nickname"],
            email=player.get("email"),
            bio=player.get("bio"),
            race=race,
            guild=guild if guild_name else None,  # Якщо гільдія відсутня, залишаємо None
            created_at=player.get("created_at")
        )


if __name__ == "__main__":
    main()
