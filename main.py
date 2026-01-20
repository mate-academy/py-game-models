import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_info = json.load(file)

    for player, info in players_info.items():
        race = info["race"]
        skills = race["skills"]
        guild = info["guild"]

        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race["name"])
                )
        try:
            if not Guild.objects.filter(name=guild["name"]).exists():
                Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )
        except TypeError:
            pass

        if not Player.objects.filter(nickname=player).exists():
            try:
                Player.objects.create(
                    nickname=player,
                    email=info["email"],
                    bio=info["bio"],
                    race=Race.objects.get(name=race["name"]),
                    guild=Guild.objects.get(name=guild["name"])
                )
            except TypeError:
                Player.objects.create(
                    nickname=player,
                    email=info["email"],
                    bio=info["bio"],
                    race=Race.objects.get(name=race["name"])
                )


if __name__ == "__main__":
    main()
