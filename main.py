import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, info in players.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )

        if created:
            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(id=race[0].id)
                )

        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        Player.objects.get_or_create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(id=race.id),
            guild=(
                Guild.objects.get(id=guild.id)
                if info["guild"] else None
            )
        )


if __name__ == "__main__":
    main()
