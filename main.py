import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
    for nickname, data in players.items():
        guild = None
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
        if data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )
        [
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race
            ) for skill in data["race"]["skills"]
        ]
        Player.objects.get_or_create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
