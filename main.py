import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source:
        data = json.load(source)

    for players_name, info in data.items():
        race = info["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        skills = info["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_obj
            )

        guild = info["guild"]
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=players_name,
            email=info["email"],
            bio=info["bio"],
            race=race_obj,
            guild=guild
        )


if __name__ == "__main__":
    main()
