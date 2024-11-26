import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        information = json.load(file)

    for player, info in information.items():
        race_info = info["race"]
        if not Race.objects.filter(name=race_info["name"]).exists():
            Race.objects.create(name=race_info["name"],
                                description=race_info["description"])
        race = Race.objects.get(name=race_info["name"])

        skills = info["race"]["skills"]
        if skills:
            for spell in skills:
                if not Skill.objects.filter(name=spell["name"]).exists():
                    Skill.objects.create(
                        name=spell["name"],
                        bonus=spell["bonus"],
                        race=race
                    )

        guild_info = info["guild"]
        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            guild = Guild.objects.get(name=guild_info["name"])
        else:
            guild = None

        gamer = information[player]
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(nickname=player,
                                  email=gamer["email"],
                                  bio=gamer["bio"],
                                  race=race,
                                  guild=guild,
                                  )


if __name__ == "__main__":
    main()
