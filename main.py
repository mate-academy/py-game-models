import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as player_json:
        player_data = json.load(player_json)

    for player_nickname, player_info in player_data.items():

        race, created = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                race=race,
                name=skill["name"],
                bonus=skill["bonus"]
            )

        if player_info["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
