import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as f:
        data = json.load(f)

    races = {
        data[player]["race"]["name"]: data[player]["race"]["description"]
        for player in data
    }

    for race in list(races.items()):
        Race.objects.create(name=race[0], description=race[1])

    skills = {
        data[player]["race"]["name"]: {
            skill["name"]: skill["bonus"]
            for skill in data[player]["race"]["skills"]
        }
        for player in data
    }

    for i in range(len(skills)):
        for skill_name, skill_bonus in list(skills.values())[i].items():
            Skill.objects.create(
                name=skill_name,
                bonus=skill_bonus,
                race=Race.objects.get(name=list(skills.keys())[i])
            )

    guilds = {
        data[player]["guild"]["name"]: data[player]["guild"]["description"]
        for player in data if data[player]["guild"]
    }

    for guild in list(guilds.items()):
        if guild[1]:
            Guild.objects.create(name=guild[0], description=guild[1])
        else:
            Guild.objects.create(name=guild[0])

    for player in data:
        if data[player]["guild"]:
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=Race.objects.get(name=data[player]["race"]["name"]),
                guild=Guild.objects.get(name=data[player]["guild"]["name"])
            )
        else:
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=Race.objects.get(name=data[player]["race"]["name"]),
                guild=None
            )


if __name__ == "__main__":
    main()
