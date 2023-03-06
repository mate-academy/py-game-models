import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json

def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
        for key in data:
            Player.objects.create(nickname=key, bio=data[key]["bio"])


if __name__ == "__main__":
    main()
