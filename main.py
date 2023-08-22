import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for player in data:
            if Player.objects.filter(nickname=player).exists():
                continue
            guild = data[player]["guild"]
            race = data[player]["race"]
            if guild is not None:
                if not Guild.objects.filter(name=guild["name"]).exists():
                    Guild.objects.create(
                        name=guild["name"],
                        description=guild["description"],
                    )
                guild = Guild.objects.filter(name=guild["name"]).get()
            if not Race.objects.filter(name=race["name"]).exists():
                Race.objects.create(
                    name=race["name"],
                    description=race["description"],
                )
            for skill in race["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.filter(name=race["name"]).get(),
                    )
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=Race.objects.filter(name=race["name"]).get(),
                guild=guild,
            )


if __name__ == "__main__":
    main()
