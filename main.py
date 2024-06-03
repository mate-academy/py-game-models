import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player_name, player_data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
        if player_data["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )
        for skill in player_data["race"]["skills"]:
            if skill is not None:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(
                        name=player_data["race"]["name"]
                    )
                )


if __name__ == "__main__":
    main()
