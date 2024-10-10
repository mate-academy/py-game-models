import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source_file:
        data = json.load(source_file)

    for player, characteristic in data.items():
        race, _ = Race.objects.get_or_create(
            name=characteristic["race"]["name"],
            description=characteristic["race"]["description"],
        )
        for skill in characteristic["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race.id
            )

        guild = Guild.objects.get_or_create(
            **characteristic["guild"]
        )[0] if characteristic["guild"] else None

        Player.objects.get_or_create(
            nickname=player,
            email=characteristic["email"],
            bio=characteristic["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
