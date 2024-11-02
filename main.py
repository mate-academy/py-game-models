import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_data:
        players_info = json.load(players_data)
    for player_name, player_data in players_info.items():
        player = Player(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={"description": player_data["race"]["description"]}
            )[0],
            guild=Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                description=player_data["guild"]["description"],
                defaults={"description": player_data["guild"]["description"]}
            )[0] if player_data.get("guild") else None,
        )
        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": player.race}
            )
        player.save()
