import init_django_orm  # noqa: F401

import json
from datetime import datetime
from db.models import Race, Skill, Guild, Player

def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        race, created_race = Race.objects.get_or_create(
            name=player_data["race_name"],
            defaults={"description": player_data.get("race_description", "")}
        )

        guild, created_guild = Guild.objects.get_or_create(
            name=player_data["guild_name"],
            defaults={"description": player_data.get("guild_description", "")}
        )

        for skill_data in player_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
            created_at=datetime.now()
        )

if __name__ == "__main__":
    main()
