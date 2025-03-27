import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def create_skill(skills: list[dict], race: Race) -> None:
    for skill in skills:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race,
        )


def create_race(race_value: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_value["name"],
        description=race_value["description"]
    )
    create_skill(race_value["skills"], race)
    return race


def create_guild(guild_value: dict) -> Guild:
    guild, created = Guild.objects.get_or_create(
        name=guild_value["name"],
        description=guild_value["description"]
    )
    return guild


def create_player(name: str, player_value: dict) -> None:
    race = create_race(player_value["race"])
    guild = None
    if player_value["guild"]:
        guild = create_guild(player_value["guild"])
    Player.objects.create(
        nickname=name,
        email=player_value["email"],
        bio=player_value["bio"],
        race=race,
        guild=guild,
    )


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_value in players.items():
        create_player(player_name, player_value)


if __name__ == "__main__":
    main()
