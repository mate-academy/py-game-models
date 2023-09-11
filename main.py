import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, player_data in players.items():
        player_race, race_created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
        if skills := player_data["race"]["skills"]:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        guild = player_data["guild"]
        if guild is not None:
            guild, guild_created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        Player.objects.get_or_create(
            nickname=name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get(name=player_data["race"]["name"]),
            guild=guild
        )


if __name__ == "__main__":
    main()
