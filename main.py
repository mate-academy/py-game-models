import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def create_race(race: dict) -> Race | bool:
    return Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )


def create_skill(skills: list[dict], race: Race) -> None:
    for skill in skills:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def create_guild(guild: dict) -> Guild | None:
    if not guild:
        return
    guild_obj, created = Guild.objects.get_or_create(
        name=guild["name"],
        description=guild["description"]
    )
    return guild_obj


def main() -> None:
    with open("players.json") as players:
        data_players = json.load(players)
    for player_name, data in data_players.items():
        race, created = create_race(data["race"])
        if created:
            create_skill(data["race"]["skills"], race)
        guild = create_guild(data["guild"])
        Player.objects.get_or_create(
            nickname=player_name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
