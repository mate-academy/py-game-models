import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players_info = json.load(json_file)

    for name, player_data in players_info.items():
        race_info = player_data.get("race")

        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            defaults={
                "description": race_info.get("description")
            }
        )
        for skill in race_info.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                race=race,
                defaults={
                    "bonus": skill.get("bonus")
                }
            )

        guild_info = player_data.get("guild")
        guild = None

        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                defaults={
                    "description": guild_info.get("description")
                }
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
