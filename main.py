import init_django_orm  # noqa: F401

import json
from pathlib import Path
from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_file = Path("players.json")
    with open(players_file, "r") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        guild = None
        if player_info["guild"]:
            guild_data = player_info["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info["email"],
                "bio": player_info["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
