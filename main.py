import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    # reading data from JSON file
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        # Create or obtain a race
        race_data = player_info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description"))

        # Create or obtain skills for that race
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race,
            )

        # Create or obtain a guild
        guild_data = player_info["guild"]
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data.get("description")
            )

        # Create a player
        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild if guild_data else None,
        )


if __name__ == "__main__":
    main()
