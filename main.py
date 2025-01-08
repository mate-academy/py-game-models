import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source_file:
        players = json.load(source_file)

    for info in players.values():
        guild = info["guild"]
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=(
                    guild["description"]
                    if guild["description"]
                    else None
                )
            )
        race = info["race"]
        if race and not Race.objects.filter(name=race["name"]).exists():
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
            race.save()
            skills = info["race"]["skills"]
            if skills:
                for skill in skills:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race_id=race.id
                    )

    for nickname, info in players.items():
        guild = info.get("guild")
        if guild:
            guild = Guild.objects.get(name=info["guild"]["name"])
        Player.objects.create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=info["race"]["name"]),
            guild=guild
        )


if __name__ == "__main__":
    main()
