import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, info in players.items():
        email = info["email"]
        bio = info["bio"]
        race_ = info["race"]
        skills = race_["skills"]
        guild_ = info["guild"]

        if not Race.objects.filter(name=race_["name"]).exists():
            Race.objects.create(
                name=race_["name"],
                description=race_["description"],
            )

        race = Race.objects.get(name=race_["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        if guild_:
            if not Guild.objects.filter(name=guild_["name"]).exists():
                Guild.objects.create(
                    name=guild_["name"],
                    description=guild_["description"]
                )

            guild = Guild.objects.get(name=guild_["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race,
                guild=guild,
            )


if __name__ == "__main__":
    main()
