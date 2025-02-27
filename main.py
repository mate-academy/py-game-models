import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for key in players.keys():
            Race.objects.get_or_create(name=players[key]["race"]["name"],
                                       description=players[key]
                                       ["race"]["description"])
            for skill in players[key]["race"]["skills"]:
                Skill.objects.get_or_create(name=skill["name"],
                                            bonus=skill["bonus"],
                                            race=Race.objects.get
                                            (name=players["race"]["name"]),)
            Guild.objects.get_or_create(name=players[key]["guild"]["name"],
                                        description=players
                                        [key]["guild"]["description"])
            Player.objects.get_or_create(nickname=key,
                                         email=players[key]["email"],
                                         bio=players[key]["bio"],
                                         race=Race.objects.get
                                         (name=players[key]["race"]["name"]),
                                         guild=Guild.objects.get
                                         (name=players[key]["guild"]["name"]),
                                         )


if __name__ == "__main__":
    main()
