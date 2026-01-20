import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for player, player_info in players_data.items():

        player_guild = player_info["guild"] if player_info["guild"] else None

        if player_guild:
            player_guild, _ = Guild.objects.get_or_create(
                name=player_guild["name"],
                description=player_guild["description"]
            )

        player_race = player_info["race"]

        Race.objects.get_or_create(
            name=player_race["name"],
            description=player_race["description"]
        )

        player_skills = player_race["skills"]

        for skill in player_skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=player_race["name"])
            )

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=Race.objects.get(name=player_race["name"]),
            guild=player_guild
        )


if __name__ == "__main__":
    main()
