import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race = player_info["race"]
        if race:
            race, information = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        guild = player_info["guild"]
        if guild:
            guild, information = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        skills = player_info["race"]["skills"]
        if skills:
            for skill in skills:
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
