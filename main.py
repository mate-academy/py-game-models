import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as players:
        game_data = json.load(players)
    for player in game_data:
        race = game_data[player]["race"]
        skills = race["skills"]
        guild = game_data[player]["guild"]

        race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name="elf")
            )

        guild = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )[0] if guild else None

        Player.objects.create(
            nickname=player,
            email=game_data[player]["email"],
            bio=game_data[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()