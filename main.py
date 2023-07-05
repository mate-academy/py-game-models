import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data:
        players = json.load(data)

    for player_name, player_data in players.items():

        race = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )[0]

        guild = Guild.objects.get_or_create(
            name=player_data["guild"]["name"],
            description=player_data["guild"]["description"]
        )[0] if player_data["guild"] else None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )

        if player_data["race"]["skills"]:
            for skill in player_data["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )


if __name__ == "__main__":
    main()
