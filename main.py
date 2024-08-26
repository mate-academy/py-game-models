import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race = get_or_create_race(player_info)
        get_or_create_player(player_name, player_info, race)
        get_or_create_skills(player_info, race)


def get_or_create_guild(player_info: dict) -> Guild | None:
    guild, _ = Guild.objects.get_or_create(
        name=player_info.get("guild").get("name"),
        description=player_info.get("guild").get("description")
    ) if player_info.get("guild") else (None, None)
    return guild


def get_or_create_player(
    player_name: str,
    player_info: dict,
    race: Race
) -> None:
    Player.objects.get_or_create(
        nickname=player_name,
        email=player_info.get("email"),
        bio=player_info.get("bio"),
        race=race,
        guild=get_or_create_guild(player_info)
    )


def get_or_create_race(player_info: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=player_info.get("race").get("name"),
        description=player_info.get("race").get("description")
    )
    return race


def get_or_create_skills(player_info: dict, race: Race) -> None:
    if player_info.get("race").get("skills"):
        for skill in player_info.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )
