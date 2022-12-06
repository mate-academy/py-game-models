import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:

    with open("players.json", "r") as f:
        user_data = json.load(f)
        for key, value in user_data.items():
            if not Race.objects.filter(name=value["race"]["name"]).exists():
                Race.objects.create(name=value["race"]["name"],
                                    description=value["race"]["description"])
                for skill in value["race"]["skills"]:
                    if not Skill.objects.filter(name=skill["name"]).exists():
                        Skill.objects.create(name=skill["name"],
                                             bonus=skill["bonus"],
                                             race=Race.objects.get
                                             (name=value["race"]["name"]))
            try:
                if not Guild.objects.filter(name=value["guild"]
                                            ["name"]).exists():
                    Guild.objects.create(name=value["guild"]["name"],
                                         description=value["guild"]
                                         ["description"])
            except TypeError:
                pass

            try:
                if not Player.objects.filter(nickname=key).exists():
                    Player.objects.create(nickname=key,
                                          email=value["email"],
                                          bio=value["bio"],
                                          race=Race.objects.get
                                          (name=value["race"]["name"]),
                                          guild=Guild.objects.get
                                          (name=value["guild"]["name"]))
            except TypeError:
                Player.objects.create(nickname=key,
                                      email=value["email"],
                                      bio=value["bio"],
                                      race=Race.objects.get
                                      (name=value["race"]["name"]))


if __name__ == "__main__":
    main()
