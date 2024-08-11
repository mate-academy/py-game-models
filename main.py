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
        create_players(player_nickname, player_info)


def create_players(player_nickname: str, player_info: dict) -> None:
    race, created = Race.objects.get_or_create(
        name=player_info.get("race").get("name"),
        defaults={"description": player_info.get("race").get("description")},
    )

    for skill in player_info.get("race").get("skills"):
        Skill.objects.get_or_create(
            name=skill.get("name"),
            race=race,
            defaults={"bonus": skill.get("bonus")}
        )

    guild_name = player_info.get("guild")
    if guild_name:
        guild, created = Guild.objects.get_or_create(
            name=guild_name.get("name"),
            defaults={
                "description": player_info.get("guild").get("description")
            }
        )
    else:
        guild = None

    Player.objects.get_or_create(
        nickname=player_nickname,
        race=race,
        guild=guild,
        defaults={
            "email": player_info.get("email"),
            "bio": player_info.get("bio"),
        }
    )
