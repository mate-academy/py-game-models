import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
        for nickname, player in players.items():
            race = player["race"]
            Race.objects.get_or_create(
                name=race["name"],
                defaults={"description": race["description"]}
            )

            skills = race["skills"]
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": Race.objects.get(name=race["name"])
                    }
                )

            guild = player["guild"]
            if guild:
                Guild.objects.get_or_create(
                    name=guild["name"],
                    defaults={
                        "description": guild["description"]
                    }
                )
                Player.objects.create(
                    nickname=nickname,
                    email=player["email"],
                    bio=player["bio"],
                    race=Race.objects.get(name=race["name"]),
                    guild=Guild.objects.get(name=guild["name"])
                )
            else:
                Player.objects.create(
                    nickname=nickname,
                    email=player["email"],
                    bio=player["bio"],
                    race=Race.objects.get(name=race["name"]),
                )


if __name__ == "__main__":
    main()
