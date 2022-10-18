import json

import init_django_orm  # noqa: F401
from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json") as data:
        users_data = json.load(data)

    for user_name, user_data in users_data.items():
        race = user_data["race"]
        skills = user_data["race"]["skills"]
        guild = user_data["guild"]

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race["name"]),
                )
        if guild is not None and \
                not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

        if user_data["guild"] is None:
            guild_instance = None
        else:
            guild_instance = Guild.objects.get(name=guild["name"])
        Player.objects.create(
            nickname=user_name,
            email=user_data["email"],
            bio=user_data["bio"],
            race=Race.objects.get(name=race["name"]),
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
