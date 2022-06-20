import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as game_data:
        players_data = json.load(game_data)
    for players in players_data:
        if not Race.objects.filter(name=players_data[players]
           ["race"]["name"]).exists():
            Race.objects.create(name=players_data[players]["race"]["name"],
                                description=players_data[players]
                                ["race"]["description"])
        if players_data[players]["guild"] is not None and \
                not Guild.objects.filter(
                    name=players_data[players]
                    ["guild"]["name"]).exists():
            Guild.objects.create(name=players_data[players]["guild"]["name"],
                                 description=players_data[players]
                                 ["guild"]["description"])
        if len(players_data[players]["race"]["skills"]) != 0:
            for skill in players_data[players]["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(name=skill["name"],
                                         bonus=skill["bonus"],
                                         race=Race.objects.get(
                                             name=players_data[players]
                                             ["race"]["name"]))
        guild_value = players_data[players]["guild"]
        Player.objects.create(nickname=players,
                              email=players_data[players]["email"],
                              bio=players_data[players]["bio"],
                              race=Race.objects.get(
                                  name=players_data[players]
                                  ["race"]["name"]),
                              guild=Guild.objects.get(
                                  name=players_data[players]
                                  ["guild"]["name"])
                              if guild_value is not None else guild_value)


if __name__ == "__main__":
    main()
