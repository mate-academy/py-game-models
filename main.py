import json
import init_django_orm  # noqa: F401

from typing import Any
from db.models import Race, Skill, Player, Guild


def load_json_data(filename: Any) -> Any:
    with open(filename, "r") as file:
        return json.load(file)


def main() -> None:
    data = load_json_data("players.json")

    for player_name, player_data in data.items():
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data.get("description")
        )

        guild_data = player_data["guild"]
        if guild_data:
            guild_name = guild_data["name"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_data.get("description", "")
            )
        else:
            guild = None

        skill_data = player_data["race"]["skills"]
        for skill_data in skill_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
