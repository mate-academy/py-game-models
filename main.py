import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def open_player_file() -> dict:
    with open("players.json") as players:
        return json.load(players)


def create_race(data: dict) -> Race:
    if not Race.objects.filter(name=data["race"]["name"]).exists():
        race = Race.objects.create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
    else:
        race = Race.objects.get(name=data["race"]["name"])
    return race


def create_skill(data: dict) -> None:
    for skill in data["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            skill = Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"]
            )
        else:
            skill = Skill.objects.get(name=skill["name"])
        skill.race = create_race(data)
        skill.save()


def create_guild(data: dict) -> None:
    guild = None
    if data["guild"] is not None:
        if not Guild.objects.filter(name=data["guild"]["name"]).exists():
            guild = Guild.objects.create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )
        else:
            guild = Guild.objects.get(name=data["guild"]["name"])
    return guild


def create_player(name: str, data: dict) -> None:
    Player.objects.create(
        nickname=name,
        email=data["email"],
        bio=data["bio"],
        race=create_race(data),
        guild=create_guild(data)
    )


def main() -> None:
    players_data = open_player_file()
    for name, data in players_data.items():
        create_race(data)
        create_skill(data)
        create_guild(data)
        create_player(name, data)


if __name__ == "__main__":
    main()
