import json
try:
    import init_django  # noqa: F401
except ImportError:
    pass

from db.models import Guild, Player, Race, Skill

# Реэкспорт моделей для тестов
__all__ = ["main", "Race", "Skill", "Player", "Guild"]


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for nickname, player_info in players_data.items():
        race_data = player_info.get("race")
        if not race_data:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

        guild = None
        if player_info.get("guild"):
            guild_data = player_info.get("guild")
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio"),
                "race": race,
                "guild": guild,
                "created_at": player_info.get("created_at"),
            },
        )


if __name__ == "__main__":
    main()
