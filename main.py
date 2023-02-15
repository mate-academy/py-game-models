import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild  # noqa: F401
from app.createBaseClasses import CreateBase


def main() -> None:
    data: dict = {}
    with open("players.json", "r") as json_file:
        data = json.load(json_file)
    for player in data.keys():
        CreateBase.create_player(
            player,
            data[player]
        )


if __name__ == "__main__":
    main()
