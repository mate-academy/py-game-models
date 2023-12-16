import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    # Use get_or_create()
    # Read data
    with open("file.json", "r") as file:
        file.read()
        data = json.load(file)





if __name__ == "__main__":
    main()
