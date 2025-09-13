import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player_name, player_data in players.items():
        race_result = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )
        if player_data["guild"]:
            guild_result = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )
            guild = guild_result[0]
        else:
            guild = None
        player = Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_result[0],
            guild=guild
        )
        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player.race
            )


if __name__ == "__main__":
    main()
