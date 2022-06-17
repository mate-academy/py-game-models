import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        players_info = json.load(file)

    for name, info in players_info.items():

        if not Race.objects.filter(name=info["race"]["name"]).exists():
            if info["race"]["description"]:
                Race.objects.create(
                    name=info["race"]["name"],
                    description=info["race"]["description"]
                )
            else:
                Race.objects.create(name=info["race"]["name"])

        race = Race.objects.get(name=info["race"]["name"])

        skills = info["race"]["skills"]
        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        if info["guild"]:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                if info["guild"]["description"]:
                    Guild.objects.create(
                        name=info["guild"]["name"],
                        description=info["guild"]["description"]
                    )
                else:
                    Guild.objects.create(name=info["guild"]["name"])

        if info["guild"]:
            guild = Guild.objects.get(name=info["guild"]["name"])
            Player.objects.create(
                nickname=name,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild
            )
        else:
            Player.objects.create(
                nickname=name,
                email=info["email"],
                bio=info["bio"],
                race=race
            )


if __name__ == "__main__":
    main()
