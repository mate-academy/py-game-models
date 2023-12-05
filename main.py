import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_json = json.load(players_file)

    for player, data in players_json.items():
        race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )[0]

        skills = data["race"]["skills"]
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild = data["guild"]
        if guild:
            guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )[0]
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
