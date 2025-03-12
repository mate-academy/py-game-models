import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for player_name, player_info in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"].get("description", "")}
        )

        guild = None
        if player_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={"description": player_info["guild"].get("description", "")}
            )

        for skill_info in player_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_info["name"],
                race=race,
                defaults={"bonus": skill_info["bonus"]}
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info.get("bio", ""),
            race=race,
            guild=guild
        )
