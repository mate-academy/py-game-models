import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)

    for player_name, information in players_dict.items():

        race, _ = Race.objects.get_or_create(
            name=information["race"]["name"],
            description=information["race"]["description"]
        )
        for skill in information["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = None
        if information["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=information["guild"]["name"],
                description=information["guild"]["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=information["email"],
            bio=information["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
