import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for key in players_data.keys():
        #  mapping guilds
        guild = players_data[key]["guild"]
        guild_obj = [None]
        if guild is not None:
            guild_obj = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        # mapping races
        race = players_data[key]["race"]
        race_object = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        # mapping skills
        if race["skills"]:
            for skill in race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_object[0]
                )

        # mapping players
        Player.objects.create(
            nickname=key,
            email=players_data[key]["email"],
            bio=players_data[key]["bio"],
            race=race_object[0],
            guild=guild_obj[0]
        )


if __name__ == "__main__":
    main()
