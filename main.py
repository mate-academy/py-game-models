import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
        for nickname, player_data in players_data.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={"description": player_data["race"]["description"]},
            )

            for skill_data in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    race=race,
                    defaults={"bonus": skill_data["bonus"]},
                )

            guild = None
            if player_data["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description": player_data["guild"]["description"]
                    },
                )

            Player.objects.get_or_create(
                email=player_data["email"],
                defaults={
                    "nickname": nickname,
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild,
                },
            )


if __name__ == "__main__":
    main()
