import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # 1. Зчитуємо JSON
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    # 2. players_data — це словник: ключ = nickname
    for nickname, data in players_data.items():

        # === RACE ===
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # === SKILLS FOR THE RACE ===
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # === GUILD (може бути None) ===
        guild = None
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # === PLAYER ===
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data.get("bio", ""),
                "race": race,
                "guild": guild,
            },
        )

    print("Дані успішно додано в базу!")


if __name__ == "__main__":
    main()
