import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as players:
        players_data = json.load(players)

    for name, data in players_data.items():
        race = data["race"]
        guild = data["guild"]
        skills = race["skills"]

        race = (
            Race.objects.get_or_create(
                name=race["name"],
                description=race["description"])
        )[0]

        if guild:
            guild = (
                Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"]
                )
            )[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.get_or_create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
