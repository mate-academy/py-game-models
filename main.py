import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player, info in players.items():
        race = info["race"]
        if not Race.objects.filter(
                name=race["name"]
        ).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"],
            )
        for skill in race["skills"]:
            if not Skill.objects.filter(
                    name=skill["name"]
            ).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=Race.objects.get(
                        name=race["name"]
                    ).id
                )
        guild = info["guild"]
        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=info["email"],
                bio=info["bio"],
                race_id=Race.objects.get(
                    name=race["name"]
                ).id,
                guild_id=Guild.objects.get(
                    name=guild["name"]
                ).id if guild else None
            )


if __name__ == "__main__":
    main()
