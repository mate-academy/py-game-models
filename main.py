import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file_in:
        players = json.load(file_in)

    for player, info_player in players.items():
        race, created = Race.objects.get_or_create(
            name=info_player["race"]["name"],
            description=info_player["race"]["description"]
        )
        for skill in info_player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        guild = None
        if info_player["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=info_player["guild"]["name"],
                description=info_player["guild"]["description"]
            )
        Player.objects.get_or_create(
            nickname=player,
            email=info_player["email"],
            bio=info_player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
