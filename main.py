import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild
from django.db.models import QuerySet


def race_create(player_race_data: dict) -> QuerySet:
    race_name = player_race_data["name"]
    if not Race.objects.filter(name=race_name).exists():
        race = Race.objects.create(name=race_name,
                                   description=player_race_data["description"])
        for skill in player_race_data["skills"]:
            Skill.objects.create(name=skill["name"],
                                 bonus=skill["bonus"],
                                 race=race)
    return Race.objects.get(name=race_name)


def guild_create(guild_data: dict) -> QuerySet | None:
    if guild_data is None:
        return None
    guild_name = guild_data["name"]
    if not Guild.objects.filter(name=guild_name).exists():
        Guild.objects.create(name=guild_name,
                             description=guild_data["description"])
    return Guild.objects.get(name=guild_name)


def main() -> None:
    with open("players.json") as config:
        players = json.load(config)
    for player, info in players.items():
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race_create(info["race"]),
            guild=guild_create(info["guild"]),
        )


if __name__ == "__main__":
    main()
