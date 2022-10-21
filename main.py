import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_info in players.items():
        race = player_info["race"]
        skills = race["skills"]
        guild = player_info["guild"]

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"],
            )
        current_race = Race.objects.get(name=race["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=current_race,
                )

        if not guild:
            current_guild = None
        else:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"],
                )
            current_guild = Guild.objects.get(name=guild["name"])

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=current_race,
            guild=current_guild,
        )


if __name__ == "__main__":
    main()
