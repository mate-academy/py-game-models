import json
import os

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open(os.path.join("players.json")) as json_file:
        players_config = json.load(json_file)

    for nickname, config in players_config.items():
        race, created = Race.objects.get_or_create(
            name=config["race"]["name"],
            description=config["race"]["description"]
        )

        if skills := config["race"].get("skills"):
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild = None
        if guild_data := config.get("guild"):
            guild, created = Guild.objects.get_or_create(**guild_data)

        Player.objects.get_or_create(
            nickname=nickname,
            email=config["email"],
            bio=config["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
