import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race = player_info["race"]
        guild = player_info["guild"] if player_info["guild"] else None
        skills = player_info["race"]["skills"]

        if not Race.objects.filter(name=race["name"]).exists():
            current_race = Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race_id=current_race.id
                    )
        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            guild = Guild.objects.get(name=guild["name"])

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=Race.objects.get(name=race["name"]),
            guild=guild
        )


if __name__ == "__main__":
    main()
