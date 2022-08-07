import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as players:
        players_info = json.load(players)

        for name, params in players_info.items():
            if not Race.objects.filter(name=params["race"]["name"]).exists():
                Race.objects.create(
                    name=params["race"]["name"],
                    description=params["race"]["description"]
                )
            for skill in params["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=params["race"]["name"])
                    )
            if params["guild"] is not None:
                if not Guild.objects.filter(
                        name=params["guild"]["name"]
                ).exists():
                    Guild.objects.create(
                        name=params["guild"]["name"],
                        description=params["guild"]["description"]
                    )
            Player.objects.create(
                nickname=name,
                email=params["email"],
                bio=params["bio"],
                race=Race.objects.get(name=params["race"]["name"]),
                guild=Guild.objects.get(name=params["guild"]["name"])
                if params["guild"] is not None
                else None
            )


if __name__ == "__main__":
    main()
