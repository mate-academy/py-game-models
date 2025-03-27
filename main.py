import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player, value in players.items():
        guild = value["guild"]
        race = value["race"]
        race_skills = value["race"]["skills"]

        if guild:
            if not Guild.objects.filter(name=guild["name"]).exists():
                guild_db = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
            else:
                guild_db = Guild.objects.get(name=guild["name"])
        else:
            guild_db = None

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

        race_db = Race.objects.get(name=race["name"])

        for skill in race_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_db
                )

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=value["email"],
                bio=value["bio"],
                race=race_db,
                guild=guild_db
            )


if __name__ == "__main__":
    main()
