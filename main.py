import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)
    for player_name, player_data in players_dict.items():
        guild = player_data["guild"]
        if player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        race = player_data["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )
        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_obj,
            guild=guild
        )


if __name__ == "__main__":
    main()
