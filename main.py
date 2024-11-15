import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    # Перевірка структури даних
    print(players_data)  # Для налагодження можна вивести дані

    for player in players_data:
        if isinstance(player, dict):  # Перевіряємо, чи це словник
            race_name = player.get("race", {}).get("name")
            race_desc = player.get("race", {}).get("description")
            race, created = Race.objects.get_or_create(
                name=race_name,
                description=race_desc
            )

            # Створюємо навички для раси, якщо вони є
            skills_data = player.get("race", {}).get("skills", [])
            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"]
                )

            guild_name = player.get("guild", {}).get("name")
            guild_desc = player.get("guild", {}).get("description")
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_desc
            )

            # Створюємо або оновлюємо гравця
            Player.objects.get_or_create(
                nickname=player["nickname"],
                email=player.get("email"),
                bio=player.get("bio"),
                race=race,
                guild=guild,
                created_at=player.get("created_at")
            )

if __name__ == "__main__":
    main()
