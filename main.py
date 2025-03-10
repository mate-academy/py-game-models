import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        players_data = json.load(file)

    for player_nick, player_description in players_data.items():

        guild = None
        guild_inf = player_description.get("guild")
        if guild_inf:
            guild = Guild.objects.get_or_create(
                name=guild_inf["name"],
                description=guild_inf["description"]
            )[0]

        race = None
        race_inf = player_description.get("race")
        if race_inf:
            race = Race.objects.get_or_create(
                name=race_inf["name"],
                description=race_inf["description"]
            )[0]

        skills = player_description["race"]["skills"]
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.get_or_create(
            nickname=player_nick,
            email=player_description["email"],
            bio=player_description["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
