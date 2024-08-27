import init_django_orm  # noqa: F401

import json
from django.utils import timezone
from db.models import Race, Skill, Player, Guild


def get_or_create_race(race_data: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]}
    )
    return race


def get_or_create_guild(guild_data: dict) -> Guild:
    if guild_data:
        guild, created = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data["description"]}
        )
        return guild


def get_or_create_player(
        player_name: str,
        player_data: dict,
        race: Race,
        guild: Guild
) -> None:
    Player.objects.get_or_create(
        nickname=player_name,
        defaults={
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild,
            "created_at": timezone.now()
        }
    )


def create_skills_for_race(skills_data: list, race: Race) -> None:
    for skill_data in skills_data:
        Skill.objects.get_or_create(
            name=skill_data["name"],
            defaults={
                "bonus": skill_data["bonus"],
                "race": race
            }
        )


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        guild_data = player_data["guild"]
        skills_data = race_data.pop("skills", [])

        race = get_or_create_race(race_data)
        guild = get_or_create_guild(guild_data)
        get_or_create_player(player_name, player_data, race, guild)
        create_skills_for_race(skills_data, race)


if __name__ == "__main__":
    main()
