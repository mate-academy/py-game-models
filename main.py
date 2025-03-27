import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player, player_data in players.items():

        player_race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"]
        )

        if len(player_data["race"]["skills"]) > 0:
            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        if player_data["guild"]:
            player_guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"]
            )
        else:
            player_guild = player_data["guild"]

        Player.objects.create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
