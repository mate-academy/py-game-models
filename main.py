import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        race, created = Race.objects.get_or_create(
            name=info["race"].get("name"),
            description=info["race"].get("description")
        )

        if created:
            for skill in info["race"].get("skills"):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild = Guild.objects.get_or_create(
            name=info["guild"].get("name"),
            description=info["guild"].get("description")
        )[0] if info["guild"] else None

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
