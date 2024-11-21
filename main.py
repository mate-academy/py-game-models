import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_description in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_description["race"]["name"],
            description=player_description["race"]["description"]
        )

        if player_description["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_description["guild"]["name"],
                description=(
                    player_description["guild"]["description"]
                    if player_description["guild"]["description"]
                    else None
                )
            )
        else:
            guild = None

        for skill in player_description["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.create(
            nickname=player_name,
            email=player_description["email"],
            bio=player_description["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()