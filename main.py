import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for nickname, player_data in players.items():

            # ----- RACE -----
            race_data = player_data["race"]

            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={
                    "description": race_data["description"]
                }
            )

            # ----- SKILL -----
            for skill_data in race_data["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={
                        "bonus": skill_data["bonus"],
                        "race": race
                    }
                )

            # ----- GUILD -----
            guild_data = player_data["guild"]
            guild = None
            if guild_data is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={
                        "description": guild_data["description"]
                    }
                )

            # ----- PLAYER -----

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": player_data["email"],
                    "bio": player_data["bio"],
                    "race": race,
                    "guild": guild,
                }
            )


if __name__ == "__main__":
    main()
