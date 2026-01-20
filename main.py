import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player_info in data.items():
        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race,
                }
            )

        guild_data = player_info.get("guild")
        guild = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data.get("description", "")}
        )[0] if guild_data else None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
