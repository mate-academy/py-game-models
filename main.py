import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.loads(players_file.read())

    for player_name, player_info in players.items():
        race = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )[0]

        guild = Guild.objects.get_or_create(
            name=player_info["guild"]["name"],
            description=player_info["guild"]["description"]
        )[0] if player_info["guild"] else None

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(**skill, race=race)

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
