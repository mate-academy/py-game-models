import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_name:
        data = json.load(file_name)

    for name, player in data.items():
        info_race = player["race"]
        if not Race.objects.filter(name=info_race["name"]).exists():
            Race.objects.create(
                name=info_race["name"],
                description=info_race["description"]
            )

        for skills in info_race["skills"]:
            if not Skill.objects.filter(
                    name=skills["name"], bonus=skills["bonus"]).exists():
                Skill.objects.create(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=Race.objects.get(name=info_race["name"])
                )

        guild_info = player["guild"]
        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )

        if not Player.objects.filter(nickname=name).exists():
            Player.objects.create(
                nickname=name,
                email=player["email"],
                bio=player["bio"],
                race=Race.objects.get(name=info_race["name"]),
                guild=(Guild.objects.get(
                    name=guild_info["name"]) if guild_info else None
                )
            )


if __name__ == "__main__":
    main()
