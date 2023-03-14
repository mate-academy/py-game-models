import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, data in players.items():
        race = data["race"]
        skills = race["skills"]
        guild = data["guild"]

        race = (Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        ))[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if guild is not None:
            guild = (Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            ))[0]

        Player.objects.get_or_create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
