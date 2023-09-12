import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        player_email = player_data["email"]
        player_bio = player_data["bio"]

        race_data = player_data["race"]

        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )

        guild_data = player_data["guild"]

        guild_obj = None
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
