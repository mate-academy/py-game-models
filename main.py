import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file:
        players = json.load(file)

    Player.objects.all().delete()

    for user_name, user_description in players.items():
        about_race = user_description["race"]
        if not Race.objects.filter(name=about_race["name"]).exists():
            Race.objects.create(
                name=about_race["name"],
                description=about_race["description"]
            )

        about_guild = user_description["guild"]
        if about_guild is not None and \
                not Guild.objects.filter(name=about_guild["name"]).exists():
            Guild.objects.create(
                name=about_guild["name"],
                description=about_guild["description"]
            )

        about_skill = user_description["race"]["skills"]
        for skill in about_skill:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=about_race["name"])
                )

        try:
            Player.objects.create(
                nickname=user_name,
                email=user_description["email"],
                bio=user_description["bio"],
                race=Race.objects.get(name=about_race["name"]),
                guild=Guild.objects.get(name=about_guild["name"])
            )
        except TypeError:
            Player.objects.create(
                nickname=user_name,
                email=user_description["email"],
                bio=user_description["bio"],
                race=Race.objects.get(name=about_race["name"])
            )


if __name__ == "__main__":
    main()
