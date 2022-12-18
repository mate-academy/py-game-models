import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_data:
        players = json.load(players_data)

    for player in players.keys():
        player_instance = Player.objects.create(
            nickname=player,
            email=players[player]["email"],
            bio=players[player]["bio"],
            race=Race.objects.get(name=players[player]["race"]["name"])
            if Race.objects.filter(name=players[player]["race"]["name"])
            else Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"] if
                players[player]["race"]["description"] else None
            ),
            guild=None if not players[player]["guild"] else
            (
                Guild.objects.get(name=players[player]["guild"]["name"])
                if Guild.objects.filter(name=players[player]["guild"]["name"])
                else Guild.objects.create(
                    name=players[player]["guild"]["name"],
                    description=players[player]["guild"]["description"]
                    if players[player]["guild"]["description"] else None
                )),
        )
        for skill in players[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]):
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_instance.race
                )


if __name__ == "__main__":
    main()
