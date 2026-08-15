import init_django_orm
import json
from django.utils import timezone
from db.models import Race, Skill, Guild, Player


def main():
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        race_name = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": ""},
        )

        guild = None
        guild_data = player_data.get("guild")
        if guild_data:
            if isinstance(guild_data, dict):
                guild_name = guild_data.get("name")
                guild_desc = guild_data.get("description")
            else:
                guild_name = guild_data
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

        skills_data = player_data.get("skills", [])
        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )


if __name__ == "__main__":
    main()
