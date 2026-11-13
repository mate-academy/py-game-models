import json
from asyncio.windows_events import NULL

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for name, player in players.items():
        if player["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]
            )

        race, _ = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"]
        )

        if player["race"]["skills"]:
            for skill_name in player["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_name["name"], bonus=skill_name["bonus"], race=race
                )

        player = Player.objects.create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
