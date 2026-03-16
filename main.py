import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

        for player_name, player_data in players_data.items():
            # Get or create Race
            race_data = player_data["race"]

            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={
                    "description": race_data["description"],
                },
            )

            # Get or create Skill
            for skill_data in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={
                        "bonus": skill_data["bonus"],
                    },
                )

            # Get or create Guild
            guild = None
            if player_data["guild"] is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description": player_data["guild"]["description"],
                    },
                )

            # Get or create Player
            Player.objects.get_or_create(
                nickname=player_name,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild,
                },
            )


if __name__ == "__main__":
    main()
