import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as script:
        players = json.load(script)

    for player, player_info in players.items():
        player_race = player_info.get("race", {})
        race, created = Race.objects.get_or_create(
            name=player_race.get("name"),
            defaults={
                "description": player_race.get("description"),
            }
        )
        for skill_data in player_race.get("skills", []):
            skill, created = Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={
                    "bonus": skill_data.get("bonus"),
                }
            )
        guild = None
        guild_data = player_info.get("guild")
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )

        Player.objects.get_or_create(
            nickname=player,
            race=race,
            guild=guild,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio"),
            }
        )


if __name__ == "__main__":
    main()
