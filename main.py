import json
from django.db import transaction
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    with transaction.atomic():
        for nickname, player_info in players_data.items():
            race, _ = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                defaults={
                    "description": player_info["race"].get("description")
                }
            )

            for skill_info in player_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    defaults={"bonus": skill_info["bonus"], "race": race})
            guild = None
            if player_info["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=player_info["guild"]["name"],
                    defaults={
                        "description": player_info["guild"].get("description")
                    }
                )

            created = Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_info["email"],
                    "bio": player_info["bio"],
                    "race": race,
                    "guild": guild
                }
            )[1]

            if created:
                print(f"Created new player: {nickname}")
            else:
                print(f"Updated existing player: {nickname}")

    print("Data import completed successfully.")


if __name__ == "__main__":
    main()
