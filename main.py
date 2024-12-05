import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():

        race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )[0] if data["race"] is not None else None

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

        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        ) if not Player.objects.filter(
            nickname=nickname
        ).exists() else None


if __name__ == "__main__":
    main()
