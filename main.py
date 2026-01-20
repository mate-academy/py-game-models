import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, player_data in players.items():
        # 1. Створення або отримання Race
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data.get(
                    "description", "")
            }
        )

        # 2. Створення або отримання Skills для Race
        if "skills" in race_data:
            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={
                        "bonus": skill_data["bonus"],
                        "race": race
                    }
                )
        # 3. Створення або отримання Guild
        if "guild" in player_data and player_data["guild"] is not None:
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get(
                        "description", ""
                    )
                }
            )
        else:
            guild = None

        # 4. Створення Player з посиланням на Race і Guild
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": None if not guild else guild
            }
        )


if __name__ == "__main__":
    main()
