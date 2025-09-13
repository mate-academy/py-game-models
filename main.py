import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player_name, player_data in players.items():
        race_data = player_data.get("race", {})
        if race_data:
            race_result = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data["description"]}
            )
        guild_data = player_data.get("guild")
        if guild_data:
            guild_result = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
            guild = guild_result[0]
        else:
            guild = None
        skills = race_data.get("skills", [])

        player = Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_result[0],
            guild=guild
        )
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": player.race
                }
            )


if __name__ == "__main__":
    main()
