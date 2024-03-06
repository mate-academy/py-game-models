import json
from datetime import datetime

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for nickname, values in players_data.items():
        race = Race.objects.get_or_create(
            name=values["race"]["name"],
            description=values["race"]["description"]
        )
        guild = Guild.objects.get_or_create(
            name=values["guild"]["name"],
            description=values["guild"]["description"]
        )[0] if values["guild"] else None

        for skill in values["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=values["race"]["name"])
            )

        guild_check = Guild.objects.get(
            id=guild[0].id
        ) if values["guild"] else None

        Player.objects.create(
            nickname=nickname,
            email=values["email"],
            bio=values["bio"],
            race=Race.objects.get(name=race[0].name),
            guild=guild_check,
            created_at=datetime.now()
        )


if __name__ == "__main__":
    main()
