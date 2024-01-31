import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for key, val in players_data.items():
        #  mapping guilds
        guild = players_data[key]["guild"]
        g = [None]
        if guild is not None:
            g = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        #mapping races
        race = players_data[key]["race"]
        r = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        #mapping skills
        if race["skills"]:
            for skill in race["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=r[0]
                )

        #mapping players
        Player.objects.create(
            nickname=key,
            email=players_data[key]["email"],
            bio=players_data[key]["bio"],
            race=r[0],
            guild=g[0]
        )


if __name__ == "__main__":
    main()
