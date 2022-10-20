import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_race(dict_race: dict) -> Race:
    race = Race.objects.get_or_create(
        name=dict_race["name"],
        description=dict_race["description"]
    )[0]
    for skill in dict_race["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )
    return race


def get_guild(dict_guild: dict) -> Guild:
    return Guild.objects.get_or_create(
        name=dict_guild["name"],
        description=dict_guild["description"]
    )[0]


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for nickname, params in data.items():
        Player.objects.get_or_create(
            nickname=nickname,
            email=params["email"],
            bio=params["bio"],
            race=get_race(params["race"]),
            guild=get_guild(params["guild"]) if params["guild"] else None
        )


if __name__ == "__main__":
    main()
