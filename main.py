import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for name, player in players.items():
        if player["guild"]:
            guild, created_guild = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"],
            )
        else:
            guild = None
        race, created_race = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"],
        )
        if player["race"]["skills"]:
            for skill in player["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )
        Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
