import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_path = Path(__file__).parent.joinpath("players.json")
    with open(players_path, "r") as file:
        players = json.load(file)

    Player.objects.all().delete()

    for nickname, player in players.items():
        player_race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )

        player_guild = None
        if player.get("guild"):
            player_guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )

        Player.objects.create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=player_race,
            guild=player_guild,
        )


if __name__ == "__main__":
    main()
