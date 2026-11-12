import json

import django

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        race_data = player_data.get("race", {})

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description", ""),
            },
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                defaults={
                    "bonus": skill_data.get("bonus"),
                    "race": race,
                },
            )

        guild_data = player_data.get("guild")

        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description"),
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    django.setup()
    main()
