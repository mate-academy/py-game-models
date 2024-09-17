import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Зчитуємо дані з файлу players.json
    with open("players.json", "r") as file:
        players_data = json.load(file)
        print(players_data)

        for nickname, player_data in players_data.items():
            # Спочатку отримуємо або створюємо расу
            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )
            # Отримуємо або створюємо гільдію
            guild_data = player_data.get("guild", None)
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            # Додаємо навички гравця
            skills_data = race_data.get("skills", [])
            for skill_data in skills_data:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data.get("bonus", "")}
                )

            # Додаємо або отримуємо гравця
            Player.objects.get_or_create(
                nickname=nickname,
                email=player_data["email"],
                bio=player_data.get("bio", ""),
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
