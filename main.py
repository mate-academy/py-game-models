import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player, description in players.items():
        race, is_created = Race.objects.get_or_create(
            name=description["race"]["name"],
            description=description["race"]["description"],
        )

        if is_created:
            skills = description["race"]["skills"]
            for skill in skills:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        guild = description["guild"] if description["guild"] else None
        if guild:
            guild, is_created = Guild.objects.get_or_create(
                name=description["guild"]["name"],
                description=description["guild"].get("description", None),
            )

        Player.objects.get_or_create(
            nickname=player,
            email=description["email"],
            bio=description["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
