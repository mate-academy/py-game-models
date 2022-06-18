import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():

        # create race
        race_name = info["race"]["name"]
        race_description = info["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        # create_skill
        skills = info["race"]["skills"]
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_name)
                )

        # create_guild
        if info["guild"]:
            guild_name = info["guild"]["name"]
            guild_description = info["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

            Player.objects.create(
                nickname=player,
                email=info["email"],
                bio=info["bio"],
                race=Race.objects.get(name=race_name),
                guild=Guild.objects.get(name=guild_name)
            )

        else:
            Player.objects.create(
                nickname=player,
                email=info["email"],
                bio=info["bio"],
                race=Race.objects.get(name=race_name),
            )


if __name__ == "__main__":
    main()
