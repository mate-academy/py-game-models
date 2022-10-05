import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file_json:
        data_json = json.load(file_json)
    for player, data in data_json.items():
        if not Race.objects.filter(name=data["race"]["name"]).exists():
            race = Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )
        else:
            race = Race.objects.get(name=data["race"]["name"])
        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        if data["guild"] is None:
            guild = None
        else:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=data["guild"]["name"])
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
