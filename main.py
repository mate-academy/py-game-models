import json

import init_django_orm  # noqa: F401
from db.models import Race, Guild, Player, Skill


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_data = player_data.get("race", {})
        skill_data = race_data.get("skills", [])
        guild_data = player_data.get("guild", {})

        race, _ = Race.objects.update_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description")
            }
        )

        for skill in skill_data:
            _, _ = Skill.objects.update_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race
                }
            )

        if guild_data and guild_data.get("name"):
            guild, _ = Guild.objects.update_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )
        else:
            guild = None

        _, _ = Player.objects.update_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
