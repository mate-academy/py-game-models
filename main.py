import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, details in players_data.items():
        race_info = details.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={"description": race_info.get("description")}
        )

        for skill_data in race_info.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race
                }
            )

        guild_info = details.get("guild")
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": details.get("email"),
                "bio": details.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
