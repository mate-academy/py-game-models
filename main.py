import json
import django
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
django.setup()


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player in data.items():
        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={
                "description": player["race"].get("description", ""),
            },
        )

        for skill in player["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill.get("bonus", ""),
                    "race": race,
                },
            )

        guild = None
        if player.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description": player["guild"].get("description", ""),
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player["email"],
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
