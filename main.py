import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for player in data:
        race = data[player]["race"]
        skills = race["skills"]
        guild = data[player]["guild"]
        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )
        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=race["name"])
                    )
        guild = Guild.objects.get(name=guild["name"]) if guild else None
        Player.objects.create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=Race.objects.get(name=race["name"]),
            guild=guild
        )


if __name__ == "__main__":
    main()
