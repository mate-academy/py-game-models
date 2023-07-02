import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players_data = json.load(json_file)

    for player in players_data:
        race = players_data[player].get("race")
        if race and not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(name=race["name"],
                                description=race["description"])
        skills = race["skills"]
        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(name=skill["name"],
                                         bonus=skill["bonus"],
                                         race_id=Race.objects.get(
                                             name=race["name"]).id)

        guild = players_data[player].get("guild")
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(name=guild["name"],
                                 description=guild["description"])

        Player.objects.create(
            nickname=player,
            email=players_data[player].get("email"),
            bio=players_data[player].get("bio"),
            race_id=Race.objects.get(name=race["name"]).id
            if race is not None else None,
            guild_id=Guild.objects.get(name=guild["name"]).id
            if guild is not None else None
        )


if __name__ == "__main__":
    main()
