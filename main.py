import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        # Load player data from players.json
        with open("players.json", "r") as file:
            players_data = json.load(file)

        # Ensure players_data is a dictionary
        if not isinstance(players_data, dict):
            raise ValueError("players.json must contain"
                             " a dictionary of players.")

        # Iterate over each player in the JSON data
        for nickname, player_data in players_data.items():
            # Ensure player_data is a dictionary
            if not isinstance(player_data, dict):
                raise ValueError(
                    f"Player data for '{nickname}' must be a dictionary."
                )

            # Get or create the Race
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                defaults={
                    "description"
                    : player_data["race"].get("description", "")
                },
            )

            # Get or create the Skills for the Race
            for skill_data in player_data["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race},
                )

            # Get or create the Guild (if the player is in a guild)
            guild = None
            if "guild" in player_data and player_data["guild"] is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    defaults={
                        "description"
                        : player_data["guild"].get("description", "")
                    },
                )

            # Get or create the Player
            Player.objects.get_or_create(
                nickname=nickname,  # Use the key as the nickname
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild,
                },
            )

    except FileNotFoundError:
        print("Error: players.json file not found.")
    except json.JSONDecodeError:
        print("Error: players.json is not a valid JSON file.")
    except KeyError as e:
        print(f"Error: Missing required key in JSON data - {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
