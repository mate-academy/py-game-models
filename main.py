import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as file_json:
        info = json.load(file_json)
        for player in info:
            if Race.objects.filter(name=info[player]["race"]["name"]).exists():
                pass
            else:
                Race.objects.create(
                    name=info[player]["race"]["name"],
                    description=info[player]["race"]["description"]
                )
            if info[player]["guild"]:
                if Guild.objects.filter(
                        name=info[player]["guild"]["name"]).exists():
                    pass
                else:
                    Guild.objects.create(
                        name=info[player]["guild"]["name"],
                        description=info[player]["guild"]["description"]
                    )

            for skill in info[player]["race"]["skills"]:
                if Skill.objects.filter(name=skill["name"],
                                        bonus=skill["bonus"]).exists():
                    pass
                else:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(
                            name=info[player]["race"]["name"])
                    )
            if info[player]["guild"]:
                Player.objects.create(
                    nickname=player,
                    email=info[player]["email"],
                    bio=info[player]["bio"],
                    race=Race.objects.get(name=info[player]["race"]["name"]),
                    guild=Guild.objects.get(name=info[player]["guild"]["name"])
                )
            else:
                Player.objects.create(
                    nickname=player,
                    email=info[player]["email"],
                    bio=info[player]["bio"],
                    race=Race.objects.get(name=info[player]["race"]["name"]),)


if __name__ == '__main__':
    main()
