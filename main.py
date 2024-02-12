import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    try:
        with open("players.json", "r") as file:
            players_data = json.load(file)

            for player_name, player_data in players_data.items():
                race_data = player_data.get("race")
                guild_data = player_data.get("guild")

                race, created = Race.objects.get_or_create(
                    name=race_data.get("name"),
                    description=race_data.get("description"),
                )

                if race_data.get("skills"):
                    for skill_data in race_data.get("skills"):
                        skill, created = Skill.objects.get_or_create(
                            name=skill_data.get("name"),
                            bonus=skill_data.get("bonus"),
                            race=race,
                        )

                if guild_data:
                    guild, created = Guild.objects.get_or_create(
                        name=guild_data.get("name"),
                        description=guild_data.get("description"),
                    )
                else:
                    guild = None

                player, created = Player.objects.get_or_create(
                    nickname=player_name,
                    email=player_data["email"],
                    bio=player_data["bio"],
                    race=race,
                    guild=guild,
                )

    except FileNotFoundError:
        raise Exception("File not found!")


if __name__ == "__main__":
    main()
