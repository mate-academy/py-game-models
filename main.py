import json

import init_django_orm  # noqa: F401
from db.models import Race, Player, Guild, Skill


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():

        race = info["race"]
        guild = info["guild"]
        skills = info["race"]["skills"]

        race_, new_race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        if guild:
            guild_, new_guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            guild_ = None

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_
                )

        Player.objects.get_or_create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race_,
            guild=guild_
        )


if __name__ == "__main__":
    main()
