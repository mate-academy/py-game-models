import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    pass
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, info in players.items():
        race_info = info["race"]
        if not Race.objects.filter(name=race_info["name"]).exists():
            race = Race.objects.create(
                name=race_info["name"],
                description=race_info["description"]
            )
        else:
            race = Race.objects.get(name=race_info["name"])

        for skill in race_info["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild_info = info["guild"]
        if guild_info:
            if not Guild.objects.filter(name=guild_info["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_info["name"],
                    description=guild_info["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_info["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
