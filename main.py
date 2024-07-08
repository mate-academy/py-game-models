import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as player_file:
        data_in_file = json.load(player_file)
    print(data_in_file)


if __name__ == "__main__":
    main()
