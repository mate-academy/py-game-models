import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_player_guild(player_info: dict) -> Guild:
    guild = player_info["guild"] if player_info["guild"] else None
    if guild:
        guild, _ = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )
    return guild


def get_player_race(player_info: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=player_info["race"]["name"],
        description=player_info["race"]["description"]
    )
    return race


def get_player_skills(player_info: dict) -> None:
    race = get_player_race(player_info)
    skills = player_info["race"]["skills"]
    for skill in skills:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def create_player(player, player_info: dict) -> None:
    guild = get_player_guild(player_info)
    race = get_player_race(player_info)
    get_player_skills(player_info)

    Player.objects.create(
        nickname=player,
        email=player_info["email"],
        bio=player_info["bio"],
        race=race,
        guild=guild
    )


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)

    for player, player_info in players_info.items():
        create_player(player, player_info)


if __name__ == "__main__":
    main()
