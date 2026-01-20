import json

import init_django_orm  # noqa: F401

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        # --- Create or get race ---
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data["description"]
            },
        )

        # --- Create or get skills for race ---
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={
                    "bonus": skill_data["bonus"]
                },
            )

        # --- Create or get guild (if exists) ---
        guild = None
        guild_data = player_data.get("guild")

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data["description"]
                },
            )

        # --- Create player ---
        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
