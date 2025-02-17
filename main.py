import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
from pathlib import Path


def main() -> None:
    # Завантаження JSON-файлу
    players_file = Path(__file__).parent / "players.json"
    with open(players_file, "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        # Створення раси
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"].get("description", "")}
        )

        # Створення навичок
        for skill_data in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        # Створення гільдії (якщо є)
        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"].get("description")}
            )

        # Створення гравця
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
