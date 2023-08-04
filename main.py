import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player, info in data.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )

        for element in info["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=element["name"],
                bonus=element["bonus"],
                race=race
            )

        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"].get("description")
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
