import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def open_player_file() -> dict:
    with open("players.json") as players:
        return json.load(players)


def create_race(data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=data["race"]["name"],
        description=data["race"]["description"]
    )
    return race


def create_skill(data: dict) -> None:
    race = create_race(data)
    for skill in data["race"]["skills"]:
        skill, _ = Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"]
        )
        skill.race = race
        skill.save()


def create_guild(data: dict) -> None:
    guild = None
    if data["guild"] is not None:
        guild, _ = Guild.objects.get_or_create(
            name=data["guild"]["name"],
            description=data["guild"]["description"]
        )
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
