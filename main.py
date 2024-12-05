import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_data in players.items():
        player_race = player_data["race"]
        player_skills = player_race["skills"]
        player_guild = player_data["guild"]

        race, _ = Race.objects.get_or_create(
            name=player_race["name"],
            defaults={"description": player_race["description"]}
        )

        for skill_data in player_skills:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

            guild = None
            if player_guild:
                guild, _ = Guild.objects.get_or_create(
                    name=player_guild["name"],
                    defaults={"description": player_guild["description"]}
                )

            Player.objects.get_or_create(
                nickname=player,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
