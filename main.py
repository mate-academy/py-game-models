import os
import django
import json
from db.models import Race, Skill, Player, Guild

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> None:
    try:
        # Зчитування JSON-файлу
        with open("players.json", "r") as file:
            players_data = json.load(file)
            print("Players data loaded successfully.")
    except FileNotFoundError:
        print("Error: players.json file not found.")
        return
    except json.JSONDecodeError:
        print("Error: players.json is not a valid JSON file.")
        return

    # Обробка даних гравців
    for player_name, player_data in players_data.items():
        # Створення Race
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # Створення Skills для Race
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        # Створення Guild, якщо є
        guild = None
        if player_data["guild"]:
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        # Створення Player
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )
        print(f"Player {player_name} processed.")


if __name__ == "__main__":
    main()
