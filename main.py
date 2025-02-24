import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def create() -> None:
    # Read the players.json data
    with open("players.json", "r") as file:
        players_data = json.load(file)

    # Traverse through each player's data
    for nickname, player_data in players_data.items():
        # Get or create the Race
        race_data = player_data["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # Get or create each Skill associated with the Race
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                }
            )

        # Get or create the Guild (it's optional for a player)
        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # Finally, create the Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }
        )


def main() -> None:
    # Call the create function to populate the database
    create()


if __name__ == "__main__":
    main()
