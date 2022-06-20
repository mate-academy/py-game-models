import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_guild(value):
    if value["guild"]:
        if not Guild.objects.filter(name=value["guild"]["name"]).exists():
            Guild.objects.create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

        return Guild.objects.get(name=value["guild"]["name"])


def get_race(value):
    if not Race.objects.filter(name=value["race"]["name"]).exists():
        Race.objects.create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

    return Race.objects.get(name=value["race"]["name"])


def set_skills(value, race):
    for skill in value["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def create_player(key, value, race, guild):
    Player.objects.create(
        nickname=key,
        email=value["email"],
        bio=value["bio"],
        race=race,
        guild=guild
    )


def main():
    with open("players.json", "r") as file:
        players = json.load(file)

    for key, value in players.items():
        guild = get_guild(value)
        race = get_race(value)
        set_skills(value, race)
        create_player(key, value, race, guild)


if __name__ == "__main__":
    main()
