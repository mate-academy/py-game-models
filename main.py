import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r")as players:
        for player_name, player_info in json.load(players).items():

            if player_info["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=player_info["guild"].get("name"),
                    description=player_info["guild"].get("description")
                )
            else:
                guild = None

            race, _ = Race.objects.get_or_create(
                name=player_info["race"].get("name"),
                description=player_info["race"].get("description"))

            for skill in player_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

            Player.objects.get_or_create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
