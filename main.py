import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        content = json.load(file)

    for player, info in content.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )

        if info["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )

        for skil in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skil["name"],
                bonus=skil["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
