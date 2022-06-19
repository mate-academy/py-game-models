import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json") as file:
        players_data = json.load(file)

    races = [players_data[element]["race"] for element in list(players_data)]
    guilds = [players_data[element]["guild"] for element in list(players_data)]
    skills = [players_data[element]["race"]["skills"]
              for element in list(players_data)]

    for race in races:
        if not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )

    for guild in guilds:
        if guild is not None and not Guild.objects.filter(
                name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

    for i in range(2):
        Skill.objects.create(
            name=skills[0][i]["name"],
            bonus=skills[0][i]["bonus"],
            race=Race.objects.get(
                name=players_data[list(players_data)[0]]["race"]["name"])
        )

    for element in list(players_data):
        if players_data[element]["guild"] is not None:
            Player.objects.create(
                nickname=element,
                email=players_data[element]["email"],
                bio=players_data[element]["bio"],
                race=Race.objects.get(
                    name=players_data[element]["race"]["name"]),
                guild=Guild.objects.get(
                    name=players_data[element]["guild"]["name"])
            )
        else:
            Player.objects.create(
                nickname=element,
                email=players_data[element]["email"],
                bio=players_data[element]["bio"],
                race=Race.objects.get(
                    name=players_data[element]["race"]["name"]),
            )
    print(list(players_data))


if __name__ == "__main__":
    main()
