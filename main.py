import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)
        for player_name, player_data in players_info.items():
            race_name = player_data["race"]["name"]
            guild_data = player_data["guild"]

            race, _ = Race.objects.get_or_create(
                name=race_name,
                description=player_data["race"]["description"]
            )

            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
                if guild_data else None
            )

            player, _ = Player.objects.get_or_create(
                name=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )

            for skill_data in player_data["race"]["skills"]:
                skill, _ = Skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race
                    if skill_data else None
                )


if __name__ == "__main__":
    main()
