import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_info in players.items():

        race_info = player_info["race"]
        if not Race.objects.filter(name=race_info["name"]).exists():
            Race.objects.create(
                name=race_info["name"],
                description=race_info["description"]
            )
        race = Race.objects.get(name=race_info["name"])

        for skills_info in race_info["skills"]:
            if not Skill.objects.filter(name=skills_info["name"]).exists():
                Skill.objects.create(
                    name=skills_info["name"],
                    bonus=skills_info["bonus"],
                    race=race
                )

        guild_info = player_info["guild"]
        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            guild = Guild.objects.get(name=guild_info["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
