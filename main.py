import init_django_orm  # noqa: F401
import json
from django.utils import timezone
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    if isinstance(data, dict):
        players_data = data.get("players", data)
    else:
        players_data = data

    for player_data in players_data:
        race_info = player_data.get("race", {})
        if isinstance(race_info, dict):
            race_name = race_info.get("name")
            race_desc = race_info.get("description", "")
            skills_list = race_info.get("skills", [])
        else:
            race_name = race_info
            race_desc = ""
            skills_list = []

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc},
        )

        guild = None
        guild_info = player_data.get("guild")
        if guild_info:
            if isinstance(guild_info, dict):
                guild_name = guild_info.get("name")
                guild_desc = guild_info.get("description")
            else:
                guild_name = guild_info
                guild_desc = None

            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_desc},
            )

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
                "created_at": timezone.now(),
            },
        )

        for skill_data in skills_list:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )


if __name__ == "__main__":
    main()
