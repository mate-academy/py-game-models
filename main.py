import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    for user_name, user_info in players.items():

        race, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"],
        )
        for skill in user_info["race"]["skills"]:
            if skill:
                skill, _ = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        guild_info = user_info["guild"]
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"],
            )

        Player.objects.get_or_create(
            nickname=user_name,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
