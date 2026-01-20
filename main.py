import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, data in data.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"])

        for skill in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = Guild.objects.get_or_create(
            name=data["guild"]["name"],
            description=data["guild"]["description"]
        )[0] if data["guild"] is not None else None

        Player.objects.get_or_create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
