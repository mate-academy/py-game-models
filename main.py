import json
from typing import Any

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

PATH_DATA = "players.json"


def read_json(path_data: str) -> Any:
    with open(path_data, "r") as file:
        return json.load(file)


def populate_model_fields(players_data: dict) -> None:
    for nickname, player_data in players_data.items():

        race_data = player_data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        skills_data = race_data.get("skills", [])
        for skill_data in skills_data:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data.get("name"),
                bonus=skill_data.get("bonus"),
                race=race
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )


def main() -> None:
    data = read_json(PATH_DATA)
    populate_model_fields(data)


if __name__ == "__main__":
    main()
