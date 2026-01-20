import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_dict:
        players = json.load(players_dict)

    for player, player_info in players.items():

        if not Race.objects.filter(name=player_info["race"]["name"]).exists():
            race = Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

            skills_list = player_info["race"]["skills"]

            if skills_list:
                for skill in skills_list:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        guild = None
        if player_info["guild"]:
            if not Guild.objects.filter(
                    name=player_info["guild"]["name"]
            ).exists():
                guild = Guild.objects.create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"],
                )
            else:
                guild = Guild.objects.get(name=player_info["guild"]["name"])

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=Race.objects.get(name=player_info["race"]["name"]),
            guild=guild
        )


if __name__ == "__main__":
    main()
