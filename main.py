import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player, player_info in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={
                "description": player_info["race"]["description"],
            },
        )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race
                }
            )
        guild = player_info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={
                    "description": player_info["guild"]["description"]
                }
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
