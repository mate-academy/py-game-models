import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("db/data/races.json") as f:
        players_data = json.load(f)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={
                "description": player_data["race"].
                get("description", "")
            }
        )

        guild = None
        if player_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={
                    "description": player_data["guild"].
                    get("description", None)
                }
            )

        skill_objects = []
        for skill_data in player_data.get("skills", []):
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data.get("bonus", ""),
                    "race": race,
                }
            )
            skill_objects.append(skill)

        player, created = Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )

    print("Database population complete!")


if __name__ == "__main__":
    main()
