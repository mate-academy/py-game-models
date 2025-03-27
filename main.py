import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for name_player, parameters in players.items():
        race = parameters["race"]
        skills = parameters["race"]["skills"]
        guild = parameters["guild"]

        race_case, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_case
                )

        if parameters["guild"]:
            guild_case, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        guild = guild_case if guild else None

        Player.objects.get_or_create(
            nickname=name_player,
            email=parameters["email"],
            bio=parameters["bio"],
            race=race_case,
            guild=guild
        )


if __name__ == "__main__":
    main()
