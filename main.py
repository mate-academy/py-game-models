import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for key, value in players_data.items():

        guild = value["guild"]
        guild_obj = None

        if guild:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        race = value["race"]
        race_object = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if race["skills"]:
            for skill in race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_object[0]
                )

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race_object[0],
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
