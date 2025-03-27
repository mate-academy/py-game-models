import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_name:
        data = json.load(file_name)

    for name, player in data.items():
        info_race = player["race"]
        Race.objects.get_or_create(
            name=info_race["name"],
            description=info_race["description"]
        )

        for skills in info_race["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=Race.objects.get(name=info_race["name"])
            )

        guild_info = player["guild"]
        if guild_info:
            Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        Player.objects.get_or_create(
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
