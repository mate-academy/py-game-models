import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        with open("players.json", "r") as file:
            players = json.load(file)
    except FileNotFoundError as e:
        print(e)

    for player_nickname, player_info in players.items():
        race = get_race(player_info)
        create_skills(race, player_info)
        guild = get_guild(player_info)

        Player.objects.get_or_create(
            nickname=player_nickname,
            race=race,
            guild=guild,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio"),
            }
        )


def get_race(player_info: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=player_info.get("race").get("name"),
        defaults={"description": player_info.get("race").get("description")},
    )
    return race


def create_skills(race: Race, player_info: dict) -> None:
    for skill in player_info.get("race").get("skills"):
        Skill.objects.get_or_create(
            name=skill.get("name"),
            race=race,
            defaults={"bonus": skill.get("bonus")}
        )


def get_guild(player_info: dict) -> Guild | None:
    guild = None
    guild_name = player_info.get("guild")
    if guild_name:
        guild, _ = Guild.objects.get_or_create(
            name=guild_name.get("name"),
            defaults={
                "description": player_info.get("guild").get("description")
            }
        )

    return guild
