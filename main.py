import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, params in players.items():

        race = None
        if params.get("race"):
            race, _ = Race.objects.get_or_create(
                name=params["race"].get("name"),
                description=params["race"].get("description")
            )

        for skill in params["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild = None
        if params.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=params["guild"].get("name"),
                description=params["guild"].get("description")
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=params["email"],
            bio=params["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
