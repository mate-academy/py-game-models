import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        race_data = player_data.get("race")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description"),
            },
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={
                    "bonus": skill_data.get("bonus"),
                },
            )

        guild_data = player_data.get("guild")

        if guild_data is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description"),
                },
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
