import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player, info in data.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )
        if created:
            skills = info["race"]["skills"] if info["race"]["skills"] else None
            if skills:
                for skill in skills:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )
        guild = info["guild"] if info["guild"] else None
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
