import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        data = json.load(players)

    Race.objects.filter().delete()
    Player.objects.filter().delete()
    Skill.objects.filter().delete()
    Guild.objects.filter().delete()

    for player in data:
        race = data[player]["race"]
        skills = race["skills"]
        guild = data[player]["guild"]

        race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name="elf")
            )

        guild = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )[0] if guild else None

        Player.objects.create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
