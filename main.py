import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, player_data in players.items():
        race = player_data["race"]
        guild = player_data["guild"]
        if not Race.objects.filter(name=race["name"]).exists():
            player_race = Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
            if race["skills"] is not None:
                for skill in race["skills"]:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(
                            name=skill["name"],
                            bonus=skill["bonus"],
                            race=player_race
                        )

        if guild is not None:
            if not Guild.objects.filter(name=guild["name"]).exists():
                guild = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            else:
                guild = Guild.objects.get(name=guild["name"])
        if not Player.objects.filter(nickname=name).exists():
            Player.objects.create(
                nickname=name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=Race.objects.get(name=race["name"]),
                guild=guild
            )


if __name__ == "__main__":
    main()
