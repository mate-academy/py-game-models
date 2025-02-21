import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def load_players():
    """Читає JSON-файл і повертає список гравців."""
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Якщо JSON має структуру словника (а не списку), конвертуємо його
    if isinstance(data, dict):
        data = [
            {
                "nickname": key,
                "email": value["email"],
                "bio": value["bio"],
                "race": value["race"],
                "guild": value["guild"]
            }
            for key, value in data.items()
        ]

    # Переконуємося, що вийшов список
    if not isinstance(data, list):
        raise ValueError("Invalid JSON structure: expected a list of players.")

    return data



def main():
    players_data = load_players()  # Отримуємо список гравців

    for player in players_data:
        # Перевіряємо, чи player має коректний формат
        if not isinstance(player, dict):
            raise ValueError(f"Invalid player data format: expected dict, got {type(player).__name__}")

        # Обробляємо расу
        race_data = player.get("race")
        if not isinstance(race_data, dict):
            raise ValueError(f"Invalid race data format: expected dict, got {type(race_data).__name__}")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", "Unknown"),
            defaults={"description": race_data.get("description", "")}
        )

        # Обробляємо скіли
        skills_data = race_data.get("skills", [])
        if not isinstance(skills_data, list):
            raise ValueError(f"Invalid skills data format: expected list, got {type(skills_data).__name__}")

        for skill_data in skills_data:
            if not isinstance(skill_data, dict):
                raise ValueError(f"Invalid skill data format: expected dict, got {type(skill_data).__name__}")

            Skill.objects.get_or_create(
                name=skill_data.get("name", "Unknown Skill"),
                race=race,
                defaults={"bonus": skill_data.get("bonus", "No bonus")}
            )

        # Обробляємо гільдію
        guild = None
        guild_data = player.get("guild")
        if guild_data:
            if not isinstance(guild_data, dict):
                raise ValueError(f"Invalid guild data format: expected dict, got {type(guild_data).__name__}")

            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", "Unknown Guild"),
                defaults={"description": guild_data.get("description", "")}
            )

        # Створюємо гравця
        Player.objects.get_or_create(
            nickname=player.get("nickname", "Unknown Player"),
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
