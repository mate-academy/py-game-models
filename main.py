import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for key, value in data.items():
        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"])

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = Guild.objects.get_or_create(
            name=value["guild"]["name"],
            description=value["guild"]["description"]
        )[0] if value["guild"] is not None else None

        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
