import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for player_name, player_data in players.items():
            player_email = player_data.get("email")
            player_bio = player_data.get("bio")
            race_info = player_data.get("race")
            guild_info = player_data.get("guild")

            race, _ = Race.objects.get_or_create(
                name=race_info.get("name"),
                description=race_info.get("description")
            )

            for skills in race_info.get("skills"):
                skill, _ = Skill.objects.get_or_create(
                    name=skills.get("name"),
                    bonus=skills.get("bonus"),
                    race=race
                )

            if guild_info:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_info.get("name"),
                    description=guild_info.get("description")
                )
            else:
                guild = None

            Player.objects.create(
                nickname=player_name,
                email=player_email,
                bio=player_bio,
                race=race,
                guild=guild
            )

    if __name__ == "__main__":
        main()


