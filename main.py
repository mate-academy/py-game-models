import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(data_players: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=data_players["race"]["name"],
        description=data_players["race"]["description"]
    )
    return race


def create_skill(data_players: dict) -> None:
    for skill in data_players["race"]["skills"]:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=create_race(data_players)
        )


def create_guild(data_players: dict) -> Guild:
    guild = None
    if data_players["guild"]:
        guild, _ = Guild.objects.get_or_create(
            name=data_players["guild"]["name"],
            description=data_players["guild"]["description"]
        )
    return guild


def create_player(data_players: dict, player: str) -> None:
    Player.objects.get_or_create(
        nickname=player,
        email=data_players["email"],
        bio=data_players["bio"],
        race=create_race(data_players),
        guild=create_guild(data_players)
    )


def main() -> None:
    with open("players.json") as players:
        data_players = json.load(players)

    for player, data in data_players.items():
        create_race(data)
        create_guild(data)
        create_skill(data)
        create_player(data, player)


if __name__ == "__main__":
    main()
