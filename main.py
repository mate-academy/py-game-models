import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        all_information = json.load(file)

    for player in all_information.keys():
        player_info = all_information[player]
        some_race, created = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"],
        )

        for skil in player_info["race"]["skills"]:
            if not Skill.objects.get(name=skil["name"]):
                Skill.objects.get_or_create(
                    name=skil["name"],
                    bonus=skil["bonus"],
                    race=some_race
                )

        if player_info["guild"] is None:
            some_guild = None

        else:
            some_guild, created = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"],
            )

        Player.objects.get_or_create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=some_race,
            guild=some_guild
        )


if __name__ == "__main__":
    main()
