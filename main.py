import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_uniq_name, all_data_of_player in data.items():

        race, status = Race.objects.get_or_create(
            name=all_data_of_player["race"]["name"],
            description=all_data_of_player["race"]["description"],
        )
        for skill in all_data_of_player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild, status = Guild.objects.get_or_create(
            name=all_data_of_player["guild"]["name"],
            description=all_data_of_player["guild"]["description"]
        ) if all_data_of_player["guild"] else (None, status)

        Player.objects.create(
            nickname=player_uniq_name,
            email=all_data_of_player["email"],
            bio=all_data_of_player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
