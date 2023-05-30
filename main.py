import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as data:
        users_data = json.load(data)
        for nickname, other_data in users_data.items():
            Player.objects.create(
                nickname=nickname,
                email=other_data["email"],
                bio=other_data["bio"]
            )


if __name__ == "__main__":
    main()
