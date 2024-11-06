from django.db import transaction

import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    with transaction.atomic():
        for nickname, player_data in players_data.items():
            race_data = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")}
            )

            for skill_data in race_data.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]}
                )

            guild = None
            if player_data.get("guild"):
                guild_data = player_data["guild"]
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")}
                )
            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()