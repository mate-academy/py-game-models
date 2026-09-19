import json
from db.models import Guild
from db.models import Player
from db.models import Race
from db.models import Skill
import init_django_orm  # noqa: F401


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_nickname, player_data in data.items():
        race_data = player_data.get("race", {})
        race_obj, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description", "")
            }
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race_obj
                }
            )

        guild_obj = None
        guild_name = player_data.get("guild")
        if guild_name:
            if isinstance(guild_name, dict):
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_name.get("name"),
                    defaults={
                        "description": guild_name.get("description")
                    }
                )
            else:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_name
                )

        Player.objects.get_or_create(
            nickname=player_nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race_obj,
                "guild": guild_obj
            }
        )


if __name__ == "__main__":
    main()
