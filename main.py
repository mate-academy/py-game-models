import json
import os

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with (open(os.path.join(os.path.dirname(__file__), "players.json"), "r")
          as file):
        players_data = json.load(file)

    for player, info in players_data.items():
        race_data = info.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill_description in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_description["name"],
                bonus=skill_description["bonus"],
                race=race
            )

        guild_data = info.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
