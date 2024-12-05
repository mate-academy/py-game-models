from __future__ import annotations
from typing import Any

import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def model_instance_from_dict(model: str, data: dict) -> Any | None:
    models = {"Race": Race, "Skill": Skill, "Player": Player, "Guild": Guild}
    class_ = models.get(model.capitalize())
    if class_ is not None and data is not None:
        return class_.objects.get_or_create(**data)[0]
    return data


def main() -> None:
    with open("players.json", "r") as file_players:
        players_data = json.load(file_players)

    for player_name, player_data in players_data.items():
        player = {"nickname": player_name}
        skills = player_data["race"].pop("skills")

        for field, data in player_data.items():
            player[field] = model_instance_from_dict(field, data)

        for skill in skills:
            skill["race"] = player["race"]
            model_instance_from_dict("skill", skill)

        model_instance_from_dict("player", player)


if __name__ == "__main__":
    main()
