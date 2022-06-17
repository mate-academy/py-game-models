import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main():
    with open("players.json") as file:
        p_info = json.load(file)

    for name in p_info:

        if Race.objects.filter(name=p_info[name]["race"]["name"]).exists():
            race = Race.objects.get(name=p_info[name]["race"]["name"])
        else:
            Race.objects.create(name=p_info[name]["race"]["name"],
                                description=p_info[name]["race"][
                                    "description"])
            race = Race.objects.get(name=p_info[name]["race"]["name"])

        for skill in p_info[name]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race=race)

        if p_info[name]["guild"]:
            if Guild.objects.filter(
                    name=p_info[name]["guild"]["name"]
            ).exists():
                guild = Guild.objects.get(name=p_info[name]["guild"]["name"])
            else:
                Guild.objects.create(
                    name=p_info[name]["guild"]["name"],
                    description=p_info[name]["guild"]["description"]
                )
                guild = Guild.objects.get(name=p_info[name]["guild"]["name"])
        else:
            guild = None

        Player.objects.create(nickname=name,
                              email=p_info[name]["email"],
                              bio=p_info[name]["bio"],
                              race=race,
                              guild=guild)


if __name__ == '__main__':
    main()
