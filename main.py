import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        data = json.load(players_file)
    players = data

    for player_name, player_info in players.items():
        race_data = player_info.get("race")
        guild_data = player_info.get("guild")
        race = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description")
            },
        )[0]
        for skill in race_data.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race
                },
            )
        if guild_data is not None:
            guild = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                },
            )[0]
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio"),
                "race": race,
                "guild": guild
            },
        )


if __name__ == "__main__":
    main()
