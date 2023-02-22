import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_race_and_skills(race_data: dict, skills_data: list) -> Race:
    obj, created = Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"]
    )
    race = obj
    if created:
        for skill in skills_data:
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

    return race


def get_guild(guild_data: dict) -> Guild | None:
    if not guild_data:
        guild = None
    else:
        obj, created = Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"]
        )
        guild = obj

    return guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_info in data.items():

        race_data = player_info["race"]
        skills_data = race_data["skills"]
        guild_data = player_info["guild"] if player_info["guild"] else None

        race = get_race_and_skills(race_data, skills_data)
        guild = get_guild(guild_data)

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
