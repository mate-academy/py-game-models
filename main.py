import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for nickname, player in players.items():
        guild_data = player["guild"]
        race_data = player["race"]
        guild = None
        race = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            if race_data["skills"]:
                for skill in race_data["skills"]:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
