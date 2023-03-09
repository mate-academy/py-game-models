import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_info in data.items():
        race = player_info["race"]
        skills = player_info["race"]["skills"]
        guild = player_info["guild"]

        race, created = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        for skill in skills:
            skill, created = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
