import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        race_info = player_data["race"]
        skill_info = race_info["skills"]
        guild_info = player_data["guild"]

        Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )
        if skill_info:
            for skill in skill_info:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_info["name"])
                )
        guild_name = None
        if guild_info:
            Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )
            guild_name = Guild.objects.get(name=guild_info["name"])

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=race_info["name"]),
            guild=guild_name,
        )


if __name__ == "__main__":
    main()
