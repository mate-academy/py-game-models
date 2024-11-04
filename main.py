import json
from db.models import Race, Skill, Player, Guild


def read_file() -> object:
    try:
        with open("players.json", "r") as players_file:
            return json.load(players_file)
    except FileNotFoundError:
        print("Error: The file 'players.json' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to parse 'players.json'."
              " The file may be corrupted.")
        return None
    except IOError:
        print("Error: Unable to read 'players.json' due to an I/O issue.")
        return None


def main() -> None:
    players_data = read_file()

    if not isinstance(players_data, dict):
        print("Error: The data from 'players.json'"
              " is not in the expected dictionary format.")
        return

    for player_name, player_data in players_data.items():
        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        race_data = player_data.get("race")
        if race_data:
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description")}
            )

            skills = []
            for skill_data in race_data.get("skills", []):
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={"bonus": skill_data["bonus"], "race": race}
                )
                skills.append(skill)

        player, created = Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
