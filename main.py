import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

        for player_key, player_data in players.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={
                    "description": player_data["race"]["description"],
                }
            )

            guild = None
            if player_data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description": player_data["guild"]["description"]
                    }
                )

            for skill in player_data["race"].get("skills"):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": race
                    }
                )

            Player.objects.get_or_create(
                nickname=player_key,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
