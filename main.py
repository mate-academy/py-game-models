import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json') as f:
        data = json.load(f)

    for nickname in data.keys():
        player = data[nickname]
        if player["guild"]:
            if not Guild.objects.filter(name=player["guild"]["name"]).exists():
                Guild.objects.create(
                    name=player["guild"]["name"],
                    description=player["guild"]["description"]
                )

        if player["race"]:
            if not Race.objects.filter(name=player["race"]["name"]).exists():
                Race.objects.create(
                    name=player["race"]["name"],
                    description=player["race"]["description"]
                )

        if player["race"]["skills"]:
            for skill in player["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=player["race"]["name"]))

        if player["guild"]:
            Player.objects.create(nickname=nickname,
                                  email=player["email"],
                                  bio=player["bio"],
                                  race=Race.objects.get(
                                      name=player["race"]["name"]),
                                  guild=Guild.objects.get(
                                      name=player["guild"]["name"])
                                  )
        else:
            Player.objects.create(nickname=nickname,
                                  email=player["email"],
                                  bio=player["bio"],
                                  race=Race.objects.get(
                                      name=player["race"]["name"])
                                  )


if __name__ == "__main__":
    Player.objects.all().delete()
    main()
    print(Player.objects.values_list(
        "nickname", "email", "bio", "race__name", "guild__name"))
