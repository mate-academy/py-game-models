import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

from json import load


def main():
    with open("players.json") as file:
        players = load(file)

    for person in players:
        player = players[person]
        if not Player.objects.filter(nickname=person).exists():
            if not Race.objects.filter(name=player["race"]["name"]):
                Race.objects.create(name=player["race"]["name"],
                                    description=player["race"]["description"])

            for skill in player["race"]["skills"]:
                print(skill["name"])
                if not Skill.objects.filter(name=skill["name"]):
                    Skill.objects.create(name=skill["name"],
                                         bonus=skill["bonus"],
                                         race=Race.objects.get(
                                             name=player["race"]["name"]))

            if player["guild"] and not Guild.objects.filter(
                    name=player["guild"]["name"]).exists():
                Guild.objects.create(name=player["guild"]["name"],
                                     description=player["guild"]
                                     ["description"])

            try:
                Player.objects.create(nickname=person,
                                      email=player["email"],
                                      bio=player["bio"],
                                      race=Race.objects.get(
                                          name=player["race"]["name"]),
                                      guild=Guild.objects.get(
                                          name=player["guild"]["name"]))
            except TypeError:
                Player.objects.create(nickname=person,
                                      email=player["email"],
                                      bio=player["bio"],
                                      race=Race.objects.get(
                                          name=player["race"]["name"]))


if __name__ == "__main__":
    main()
