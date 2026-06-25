import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_player(player_name: str, player_data: dict) -> None:
    if not isinstance(player_data, dict):
        raise ValueError("Player data must be a dict")

    email = player_data.get("email")
    bio = player_data.get("bio")

    race_data = player_data.get("race")
    if race_data is None:
        raise ValueError("Race must be provided for each player")
    if not isinstance(race_data, dict):
        raise ValueError("Race data must be a dict")
    race = create_race(race_data)

    guild_data = player_data.get("guild")
    if guild_data is not None:
        if not isinstance(guild_data, dict):
            raise ValueError("Guild data must be a dict")
        guild = create_guild(guild_data)
    else:
        guild = None

    Player.objects.create(
        nickname=player_name,
        email=email,
        bio=bio,
        race=race,
        guild=guild
    )


def create_race(race_data: dict) -> Race:
    name = race_data.get("name")
    description = race_data.get("description", "")

    race, _ = Race.objects.get_or_create(
        name=name,
        defaults={
            "description": description
        }
    )

    skills = race_data.get("skills", [])
    for skill in skills:
        create_skill(race, skill)

    return race


def create_skill(race: Race, skill_data: dict) -> None:
    name = skill_data.get("name")
    bonus = skill_data.get("bonus")

    Skill.objects.get_or_create(
        name=name,
        defaults={
            "bonus": bonus,
            "race": race
        }
    )


def create_guild(guild_data: dict) -> Guild:
    name = guild_data.get("name")
    description = guild_data.get("description")

    guild, _ = Guild.objects.get_or_create(
        name=name,
        defaults={
            "description": description
        }
    )

    return guild


def main() -> None:
    with open("players.json", mode="r", encoding="utf-8") as file:
        data: dict = json.load(file)

    if not data or not isinstance(data, dict):
        raise ValueError("Data must be a dict")

    for player_name, player_data in data.items():
        create_player(player_name, player_data)


if __name__ == "__main__":
    main()
