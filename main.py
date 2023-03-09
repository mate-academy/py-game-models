import json
from typing import List

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

with open("players.json") as data:
    DATA = json.load(data)


def main() -> None:
    for user_name, user_data in DATA.items():
        race, _ = Race.objects.get_or_create(
            name=user_data.get("race").get("name"),
            description=user_data.get("race").get("description")
        )
        for skill in user_data.get("race").get("skills"):
            Skill.objects.get_or_create(
                skill.get("name")
            )

        Player(
            nickname=user_name,
            email=user_data.get("email"),
            bio=user_data.get("bio"),
            race=race
        )


if __name__ == "__main__":
    main()
