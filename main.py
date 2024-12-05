import init_django_orm  # noqa: F401

import json
from datetime import datetime

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_nickname, player in players_data.items():

        # Creating a race

        race_name = player.get("race", {}).get("name")
        race_description = player.get("race", {}).get("description")

        if race_description:
            race_obj, race_created = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )
        elif race_description is None:
            race_obj, race_created = Race.objects.get_or_create(name=race_name)

        # Creating skills

        for skill in player.get("race", {}).get("skills"):
            skill_name = skill.get("name")
            skill_bonus = skill.get("bonus")

            skill, skill_created = Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race_obj
            )

        # Creating a guild

        if player.get("guild") is not None:
            guild_name = player.get("guild", {}).get("name")
            guild_description = player.get("guild", {}).get("description")

            guild_obj, guild_created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        # Creating a player

        player_email = player.get("email")
        player_bio = player.get("bio")

        player_obj = Player.objects.create(
            nickname=player_nickname,
            email=player_email,
            bio=player_bio,
            race=race_obj,
            guild=guild_obj if player.get("guild") is not None else None,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        print(player_obj)


if __name__ == "__main__":
    main()
