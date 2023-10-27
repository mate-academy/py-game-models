import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_info:
        players_data = json.load(players_info)

    for player_name, player_data in players_data.items():

        guild = player_data.get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        race = player_data.get("race")
        if race:
            race, created = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

        skills = player_data["race"]["skills"]
        if skills:
            for skill in skills:
                skill, created = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
