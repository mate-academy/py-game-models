import os
import init_django_orm  # noqa: F401
import json
from django.db import IntegrityError
from db.models import Race, Skill, Guild, Player


def main() -> None:
    file_path = os.path.join(os.path.dirname(__file__), "db", "players.json")
    with open(file_path, "r") as file:
        players_data = json.load(file)

    for player_data in players_data:
        race_name = player_data["race"]["name"]
        guild_name = player_data["guild"]["name"] if "guild" in player_data \
            else None

        race, created = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": player_data["race"].get(
                "description", "")}
        )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        guild = None
        if guild_name:
            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": player_data["guild"].get("description", "")
                }
            )

        try:
            Player.objects.create(
                nickname=player_data["nickname"],
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )
        except IntegrityError:
            print(
                f"Player with nickname {player_data["nickname"]} "
                "already exists."
            )


if __name__ == "__main__":
    main()
