import json
from django.db import transaction
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)
    with transaction.atomic():
        for nickname, player_data in players_data.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={
                    "description": player_data["race"].get(
                        "description", ""
                    )
                }
            )

            guild_data = player_data.get("guild")
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")}
                )

            for skill_data in player_data["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]}
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
