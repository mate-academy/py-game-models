import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        player_data = json.load(json_file)

    for player_name, player_info in player_data.items():
        guild = player_info.get("guild")
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        race = player_info.get("race")
        if race:
            race, created = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        skills = player_info["race"]["skills"]
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
