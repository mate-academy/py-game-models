import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"]
    )
    return race


def create_skill(skill_data: dict, race: Race) -> Skill:
    skill, _ = Skill.objects.get_or_create(
        name=skill_data["name"],
        bonus=skill_data["bonus"],
        race=race
    )
    return skill


def create_guild(guild_data: dict) -> Guild:
    guild, _ = Guild.objects.get_or_create(
        name=guild_data["name"],
        description=guild_data["description"]
    )
    return guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_data = player_data["race"]
        race = create_race(race_data)

        skills_data = race_data.get("skills", [])
        skills_data = [
            create_skill(skill_data, race) for skill_data in skills_data
        ]

        guild_data = player_data.get("guild")
        guild = create_guild(guild_data) if guild_data else None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
