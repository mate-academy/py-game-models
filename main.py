import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_info in data.items():

        race_info = player_info["race"]
        Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"],
        )

        for skill in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race_info["name"])
            )

        guild_info = player_info["guild"]
        guild = None
        if guild_info:
            guild, created = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=Race.objects.get(name=race_info["name"]),
            guild=guild,
        )


if __name__ == "__main__":
    main()
