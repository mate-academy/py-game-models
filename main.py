import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def create_race(list_of_race: dict) -> Race:
    race_, create = Race.objects.get_or_create(
        name=list_of_race["name"],
        description=list_of_race["description"]
    )
    return race_


def create_skill(list_of_skill: dict) -> None:
    for skills in list_of_skill["skills"]:
        if not Skill.objects.filter(name=skills["name"]).exists():
            Skill.objects.create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=create_race(list_of_skill)
            )


def guild_create(list_of_guild_names: dict) -> Guild | None:
    if list_of_guild_names:
        guild_, create = Guild.objects.get_or_create(
            name=list_of_guild_names["name"],
            description=list_of_guild_names["description"]
        )
        return guild_
    return None


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for players_name, players_data in players.items():
        create_skill(players_data["race"])
        if not Player.objects.filter(nickname=players_name).exists():
            Player.objects.create(
                nickname=players_name,
                email=players_data["email"],
                bio=players_data["bio"],
                race=create_race(players_data["race"]),
                guild=guild_create(players_data["guild"])
            )


if __name__ == "__main__":
    main()
