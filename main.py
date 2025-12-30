import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    file_path = "players.json"

    with open(file_path, "rb") as f:
        data = json.load(f)

    for name, player_data in data.items():
        # Отримання або створення раси
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        # Перевірка наявності гільдії та створення, якщо вона є
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description", None)
            )
        else:
            guild = None

        # Додавання гравця
        Player.objects.get_or_create(
            nickname=name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )

        # Додавання навичок до Skill class
        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
