import init_django_orm  # noqa: F401
import json
from db.models import Race, Guild, Skill, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        race_data = player_info.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={"description": race_data.get("description", "")}
        )

        skills_data = race_data.get("skills", [])
        for skill_info in skills_data:
            Skill.objects.get_or_create(
                name=skill_info.get("name"),
                race=race,  # Вказуємо расу, щоб уникнути IntegrityError
                defaults={"bonus": skill_info.get("bonus", "")}
            )

        guild = None
        guild_data = player_info.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={"description": guild_data.get("description", "")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
