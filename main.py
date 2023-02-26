import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        player_data = json.load(file)

    for player_nickname, data in player_data.items():
        if not Race.objects.filter(name=data["race"]["name"]).exists():
            race = Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )


        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        if data["guild"]:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
        else:
            guild = None

        if not Player.objects.filter(nickname=player_nickname).exists():
            Player.objects.create(
                nickname=player_nickname,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )