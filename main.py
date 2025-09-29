import json
from django.db import transaction
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    with transaction.atomic():
        for player_data in players_data:
            race_info = player_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_info["name"],
                defaults={"description": race_info.get("description", "")},
            )

            for skill_info in race_info.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    defaults={"bonus": skill_info["bonus"], "race": race},
                )

            guild_info = player_data.get("guild")
            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_info["name"],
                    defaults={"description": guild_info.get("description")},
                )
            else:
                guild = None

            Player.objects.get_or_create(
                nickname=player_data["nickname"],
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild,
                },
            )


if __name__ == "__main__":
    main()
