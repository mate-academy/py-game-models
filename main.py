import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def get_race_instance(player: dict, player_race: str) -> Race:
    race = Race.objects.get_or_create(
        name=player_race,
        defaults={"description": player["race"]["description"]}
    )
    return race[0]


def get_guild_instance(player_guild: dict) -> Guild:
    if player_guild:
        guild = Guild.objects.get_or_create(
            name=player_guild["name"],
            defaults={"description": player_guild["description"]},
        )
        return guild[0]


def main() -> None:
    with open("players.json", "r") as players_json:
        players = json.load(players_json)
    for nickname, player in players.items():

        race_instance = get_race_instance(player, player["race"]["name"])

        player_skills = player["race"]["skills"]
        for skill in player_skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_instance},
            )

        guild_instance = get_guild_instance(player["guild"])

        Player.objects.create(
            email=player["email"],
            bio=player["bio"],
            race=race_instance,
            guild=guild_instance,
            nickname=nickname,
        )
