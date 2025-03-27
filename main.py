import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player, player_info in players.items():
        player_email = player_info["email"]
        player_bio = player_info["bio"]

        player_race, created = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"]
        )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )

        player_guild = None

        if player_info["guild"]:
            player_guild, created = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                description=player_info["guild"]["description"]
            )

        Player.objects.create(
            nickname=player,
            email=player_email,
            bio=player_bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
