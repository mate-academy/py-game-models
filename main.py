import json
import init_django_orm  # noqa: F401

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_data in players_data.items():
        race_dict = player_data.get("race")
        if race_dict:
            race, _ = Race.objects.get_or_create(
                name=race_dict.get("name"),
                defaults={
                    "description": race_dict.get("description"),
                },
            )

            for skill_dict in race_dict.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill_dict.get("name"),
                    defaults={
                        "bonus": skill_dict.get("bonus"),
                        "race": race,
                    },
                )

        guild_dict = player_data.get("guild")
        if guild_dict:
            guild, _ = Guild.objects.get_or_create(
                name=guild_dict.get("name"),
                defaults={
                    "description": guild_dict.get("description"),
                },
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_name,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
