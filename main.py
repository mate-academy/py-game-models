import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        loaded_players = json.load(f)

    for player_name, player_data in loaded_players.items():  # Iterate through each player
        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],  # Access race data using player_data
            defaults={"description": player_data["race"].get("description", "")}
        )

        guild = None
        if player_data["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_data["guild"]["name"],
                defaults={"description": player_data["guild"].get("description", "")}
            )

        for skill_data in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data.get("bio", ""),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
