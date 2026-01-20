import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, info in players.items():

        new_race = info["race"]
        if Race.objects.filter(name=new_race["name"]).exists() is False:
            race = Race.objects.create(
                name=new_race["name"],
                description=new_race["description"]
            )
        else:
            race = Race.objects.get(name=new_race["name"])

        for new_skill in info["race"]["skills"]:
            if Skill.objects.filter(name=new_skill["name"]).exists() is False:
                Skill.objects.create(
                    name=new_skill["name"],
                    bonus=new_skill["bonus"],
                    race=race
                )

        new_guild = info["guild"]
        if new_guild is not None:
            if Guild.objects.filter(name=new_guild["name"]).exists() is False:
                guild = Guild.objects.create(
                    name=new_guild["name"],
                    description=new_guild["description"]
                )
            else:
                guild = Guild.objects.get(name=new_guild["name"])
        else:
            guild = None

        if Player.objects.filter(nickname=nickname).exists() is False:
            Player.objects.create(
                nickname=nickname, email=info["email"],
                bio=info["bio"], race=race, guild=guild
            )


if __name__ == "__main__":
    main()
