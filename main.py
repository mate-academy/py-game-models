import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        player_race = Race.race_import(
            race_name=player_data["race"]["name"],
            race_description=player_data["race"]["description"]
        )

        for skill in player_data["race"]["skills"]:
            Skill.skill_import(
                skill_name=skill["name"],
                skill_bonus=skill["bonus"],
                skill_race=player_race
            )

        if player_data["guild"]:
            player_guild = Guild.guild_import(
                guild_name=player_data["guild"]["name"],
                guild_description=player_data["guild"]["description"]
            )
        else:
            player_guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
