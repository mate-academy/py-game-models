import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_dict = json.load(players_file)

    for player_name, player_info in players_dict.items():

        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"].get("description")
        )

        guild, _ = Guild.objects.get_or_create(
            name=player_info["guild"]["name"],
            description=player_info["guild"].get("description")
        ) if player_info["guild"] else (None, _)

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )

        for skill in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race)


if __name__ == "__main__":
    main()
