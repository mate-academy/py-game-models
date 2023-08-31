import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as players_file:
        players_data = json.load(players_file)

    [
        Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

        for player_info in players_data.values()
    ]

    [
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=Race.objects.get(name=player_info["race"]["name"])
        )

        for player_info in players_data.values()
        for skill in player_info["race"]["skills"]

    ]

    [
        Guild.objects.get_or_create(
            name=player_info["guild"]["name"],
            description=player_info["guild"]["description"]
        )

        for player_info in players_data.values()
        if player_info["guild"]

    ]

    [
        Player.objects.get_or_create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=Race.objects.get(name=player_info["race"]["name"]),
            guild=Guild.objects.get(
                name=player_info["guild"]["name"]
            )
            if player_info["guild"] else None
        )

        for player_nickname, player_info in players_data.items()

    ]


if __name__ == "__main__":
    main()
