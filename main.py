import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_json = json.load(file)

    for player_name, player_info in players_json.items():

        player_race, _ = Race.objects.get_or_create(
            name=player_info["race"].get("name"),
            description=player_info["race"].get("description"),
        )
        player_skills_list = player_info["race"].get("skills")

        for skill in player_skills_list:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=player_race,
            )

        if player_info.get("guild") is not None:
            player_guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"].get("name"),
                description=player_info["guild"].get("description"),
            )
        else:
            player_guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=player_race,
            guild=player_guild,
        )
