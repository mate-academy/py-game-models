import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild
from django.db.models import QuerySet


def create_or_get_race(race_data: dict) -> QuerySet:
    race_name = race_data["name"]
    race, created = Race.objects.get_or_create(name=race_name, defaults={
        "description": race_data["description"]
    })
    if created:
        for skill_data in race_data["skills"]:
            Skill.objects.create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )
    return race


def create_or_get_guild(guild_data: dict) -> QuerySet | None:
    if guild_data is None:
        return None
    guild_name = guild_data["name"]
    guild, created = Guild.objects.get_or_create(name=guild_name, defaults={
        "description": guild_data["description"]
    })
    return guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for player_name, player_data in players_data.items():
        race = create_or_get_race(player_data["race"])
        guild = create_or_get_guild(player_data["guild"])
        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
