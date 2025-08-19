import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    # Проходимо по словнику, де ключ — нікнейм гравця
    for nickname, entry in players_data.items():
        entry["nickname"] = nickname  # Додаємо нікнейм у словник гравця

        # Race
        race_data = entry["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # Skills
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # Guild
        guild = None
        guild_data = entry.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": entry["email"],
                "bio": entry["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
