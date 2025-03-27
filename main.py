import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player_name, player_info in players_data.items():
        race_info = player_info["race"]
        guild_info = player_info["guild"]
        skills_info = race_info["skills"]
        guild = None
        race = None

        if race_info:
            race = Race.objects.get_or_create(
                name=race_info["name"],
                description=race_info["description"]
            )[0]

        if guild_info:
            guild = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )[0]

        for skill in skills_info:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
