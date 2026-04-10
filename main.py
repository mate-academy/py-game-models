import json
import init_django_orm  # noqa: F401
from django.db import transaction
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        game_data = json.load(file)

    with transaction.atomic():
        for nickname, player in game_data.items():
            email = player.get("email", "")
            bio = player.get("bio", "")
            race_data = player.get("race", "")
            race_obj, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={
                    "description": race_data.get("description", "")
                }
            )
            for skill in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill.get("bonus", ""),
                        "race": race_obj,
                    }
                )
            guild_obj = None
            if player.get("guild"):
                guild_data = player["guild"]
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={
                        "description": guild_data.get("description", "")
                    }
                )
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": email,
                    "bio": bio,
                    "race": race_obj,
                    "guild": guild_obj,
                }
            )


if __name__ == "__main__":
    main()
