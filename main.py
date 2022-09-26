import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    with open("players.json", "r") as players:
        players = json.load(players)

    for player in players:
        # Filling in the Race table
        player_temp = players[player]["race"]
        if Race.objects.filter(
                name=player_temp["name"]).exists() is False:
            Race.objects.create(
                name=player_temp["name"],
                description=player_temp["description"])

        # Filling in the Skill table
        player_temp = players[player]["race"]["skills"]
        if len(player_temp) != 0:
            for i in range(2):
                if Skill.objects.filter(
                        name=player_temp[i]["name"]).exists() is False:
                    Skill.objects.create(
                        name=player_temp[i]["name"],
                        bonus=player_temp[i]["bonus"],
                        race=Race.objects.get(name="elf"))

        # Filling in the Guild table
        player_temp = players[player]["guild"]
        if player_temp is not None:
            if Guild.objects.filter(
                    name=player_temp["name"]).exists() is False:
                Guild.objects.create(
                    name=player_temp["name"],
                    description=player_temp["description"]
                    if player_temp is not None
                    else None)

        # Filling in the Player table
        Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=Race.objects.get(name=players[player]["race"]["name"]),
            guild=Guild.objects.get(name=player_temp["name"])
            if player_temp is not None
            else None
        )


if __name__ == "__main__":
    main()
