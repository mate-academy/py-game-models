import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, info in players.items():

        if info.get("guild"):

            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            guild = Guild.objects.get(name=info["guild"].get("name"))
        else:
            guild = None

        if not Race.objects.filter(name=info["race"]["name"]).exists():

            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )

            race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"].get("skills"):
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    race=race,
                    bonus=skill["bonus"]
                )

        Player.objects.create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )
