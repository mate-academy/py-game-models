import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        player_race = player_data["race"]
        player_guild = player_data["guild"]

        get_player_race = create_race(player_race=player_race)
        create_skills(player_race=player_race, race_instance=get_player_race)
        guild = create_guild(player_guild=player_guild)

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=get_player_race,
            guild=guild
        )


def create_race(player_race: dict[str]) -> Race:
    """
    Creating unique race name, description of race and writes race to DB
    :return: Race instance
    """
    get_player_race, _ = Race.objects.get_or_create(
        name=player_race["name"],
        description=player_race["description"]
    )
    return get_player_race


def create_skills(player_race: dict[str], race_instance: Race) -> None:
    """
    Creating unique skills that are attached to the Race instance
    """
    for skill in player_race["skills"]:
        skill, _ = Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race_instance
        )


def create_guild(player_guild: dict[str]) -> Guild:
    """
    Creating unique guild name if player has a guild,
    description(not required) and writes guild to DB
    :return: Guild instance
    """
    guild = None
    if player_guild is not None:
        guild, _ = Guild.objects.get_or_create(
            name=player_guild["name"],
            description=player_guild["description"]
        )
    return guild
