import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for key, value in data.items():
        race_data = value["race"] if value["race"] else None
        if not Race.objects.filter(name=race_data["name"]).exists():
            Race.objects.create(
                name=race_data["name"],
                description=race_data["description"])
            for skill in race_data["skills"]:
                print(skill)
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_data["name"]))

        guild_data = value["guild"] if value["guild"] else None
        if value["guild"] is not None:
            if not Guild.objects.filter(name=guild_data["name"]).exists():
                Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"])

        if not Player.objects.filter(nickname=key).exists():
            Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=Race.objects.get(name=race_data["name"]),
                guild=Guild.objects.get(name=guild_data["name"])
                if value["guild"] else None)


if __name__ == "__main__":
    main()
