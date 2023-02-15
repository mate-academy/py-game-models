import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild  # noqa: F401
from app.createBaseClasses import CreateBase


def main() -> None:
    with open("players.json", "r") as json_file:
        loaded_json: dict = json.load(json_file)
        for player in loaded_json.keys():
            CreateBase.create_player(
                player,
                loaded_json[player]
            )


if __name__ == "__main__":
    main()
