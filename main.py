import os
import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players = file_data("players.json")
    create_db(players)


def create_db(players: dict) -> None:
    for player, info in players.items():
        email_info = info.get("email")
        bio_info = info.get("bio")

        if race_info := info.get("race"):
            race_name = race_info.get("name")
            race_description = race_info.get("description")

            race, race_created = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

            if skills_info := race_info.get("skills"):
                for skill in skills_info:
                    skill_name = skill.get("name")
                    skill_bonus = skill.get("bonus")

                    Skill.objects.get_or_create(
                        name=skill_name, bonus=skill_bonus, race=race
                    )
        else:
            race = None

        if guild_info := info.get("guild"):
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")

            guild, guild_created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=email_info,
            bio=bio_info,
            race=race,
            guild=guild
        )


def file_data(path: str) -> dict:
    file_path = os.path.join(path)
    with open(file_path) as f:
        players = json.load(f)

    return players


if __name__ == "__main__":
    main()
