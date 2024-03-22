import json
import os

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:

    current_dir = os.path.dirname(__file__)

    json_file_path = os.path.join(current_dir, "players.json")

    with open(json_file_path, "r") as file:
        players = json.load(file)

    for player_name, player_info in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"]["description"]}
        )
        guild = None
        if player_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={"description": player_info["guild"]["description"]}
            )

        skills = []
        for skill_info in player_info["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={"bonus": skill_info["bonus"], "race": race}
            )
        skills.append(skill)

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
