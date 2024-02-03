import json
from datetime import datetime

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", ""),
            description=race_data.get("description", "")
        )

        guild = player_data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name", ""),
                description=guild.get("description", "")
            )

        skills = []
        for skill_data in race_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data.get("name", ""),
                bonus=skill_data.get("bonus", ""),
                race=race
            )
            skills.append(skill)

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            guild=guild,
            email=player_data.get("email", ""),
            bio=player_data.get("bio", ""),
            race=race,
            created_at=datetime.now()
        )


if __name__ == "__main__":
    main()
