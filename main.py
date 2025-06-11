import init_django_orm  # noqa: F401
import json
import os

from db.models import Race, Skill, Player, Guild
from django.utils.timezone import now


def main() -> None:
    players_path = os.path.join(os.path.dirname(__file__), "players.json")
    with open(players_path, "r") as players_file:
        players = json.load(players_file)

    for nickname, data in players.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        guild_data = data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild,
                "created_at": now()
            }
        )


if __name__ == "__main__":
    main()
