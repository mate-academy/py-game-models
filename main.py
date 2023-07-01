import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild

FILE_NAME = "players.json"


def main() -> None:
    with open(FILE_NAME, "r") as file:
        players = json.load(file)

    guilds = set()
    races = set()
    skills = set()
    players_list = []

    for nickname_, value in players.items():
        if not Player.objects.filter(nickname=nickname_).exists():
            Player.objects.create(nickname=nickname_,
                                  email=value["email"],
                                  bio=value["bio"],
                                  )

        if not Race.objects.filter(name=value["race"]["name"]).exists():
            Race.objects.create(name=value["race"]["name"],
                                description=value["race"]["description"])

        for skill in value["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     )







if __name__ == "__main__":
    main()
