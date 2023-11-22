from __future__ import annotations
from typing import Any

import json
import init_django_orm  # noqa: F401

import db.models


def model_instance_from_dict(model: str, data: dict) -> Any | None:
    if data is not None:
        class_ = getattr(db.models, model.capitalize())
        return class_.objects.get_or_create(**data)[0]
    return None


def main() -> None:
    with open("players.json", "r") as file_players:
        players_data = json.load(file_players)

    for player_name, player_data in players_data.items():
        skills = player_data["race"].pop("skills")
        race = model_instance_from_dict("race", player_data["race"])

        for skill in skills:
            skill["race"] = race
            model_instance_from_dict("skill", skill)

        player_data["nickname"] = player_name
        player_data["race"] = race
        player_data["guild"] = model_instance_from_dict("guild",
                                                        player_data["guild"])

        model_instance_from_dict("player", player_data)


if __name__ == "__main__":
    main()
