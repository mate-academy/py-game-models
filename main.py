import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, data in players_data.items():
        # 1. Обробка раси
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"].get("description", "")}
        )

        # 2. Обробка скілів для цієї раси
        for skill_data in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # 3. Обробка гільдії (може бути відсутня у json)
        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"].get("description")}
            )

        # 4. Створення гравця
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
