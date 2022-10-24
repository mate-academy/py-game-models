import json

from django.db import IntegrityError

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race = player_data["race"]
        skills = race["skills"]
        guild = player_data["guild"]

        race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )[0] if guild else None

        try:
            Player.objects.create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )
        except IntegrityError:
            print(f'A player with name {player_name} already exists! Choose another nickname.')


if __name__ == "__main__":
    main()
