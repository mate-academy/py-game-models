import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def read_json(file_name) -> dict:
    with open(file_name) as file:
        return json.load(file)


def create_race(info):
    if not Race.objects.filter(name=info["race"]["name"]).exists():
        if info["race"]["description"]:
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
        else:
            Race.objects.create(name=info["race"]["name"])

    race = Race.objects.get(name=info["race"]["name"])

    return race


def create_skill(info, race):
    skills = info["race"]["skills"]
    if skills:
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


def create_guild(info):
    if info["guild"]:
        if not Guild.objects.filter(name=info["guild"]["name"]).exists():
            if info["guild"]["description"]:
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            else:
                Guild.objects.create(name=info["guild"]["name"])
        return Guild.objects.get(name=info["guild"]["name"])


def main():
    file_name = "players.json"
    players_info = read_json(file_name)

    for name, info in players_info.items():

        race = create_race(info)

        create_skill(info, race)

        guild = create_guild(info)

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )



if __name__ == "__main__":
    main()
