import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        race = player_data["race"]
        guild = player_data["guild"]
        skills = player_data["race"]["skills"]

        if race:
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )

        if skills:
            for skill in skills:
                skill, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
