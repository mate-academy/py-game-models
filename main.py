import init_django_orm  # noqa: F401
import json

from db.models import (Race, Skill, Player, Guild)


def main() -> None:

    with open("players.json", "r") as f:
        players = json.load(f)

        Race.objects.all().delete()
        previous_race_name = ""
        for player in players:
            if players[player]["race"]["name"] == previous_race_name:
                continue
            Race.objects.create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]
            )
            previous_race_name = players[player]["race"]["name"]

        Skill.objects.all().delete()
        prev = []
        for player in players:
            for i, skill in enumerate(players[player]["race"]["skills"]):
                if players[player]["race"]["skills"][i]["name"] in prev:
                    continue
                race = Race.objects.get(name=players[player]["race"]["name"])
                Skill.objects.create(
                    name=players[player]["race"]["skills"][i]["name"],
                    bonus=players[player]["race"]["skills"][i]["bonus"],
                    race=race
                )
                prev.append(players[player]["race"]["skills"][i]["name"])

        Guild.objects.all().delete()
        previous_guild_name = ""
        for player in players:
            if players[player]["guild"] is None:
                continue
            if players[player]["guild"]["name"] == previous_guild_name:
                continue
            Guild.objects.create(
                name=players[player]["guild"]["name"],
                description=players[player]["guild"]["description"]
            )
            previous_guild_name = players[player]["guild"]["name"]

        for player in players:
            race = Race.objects.get(name=players[player]["race"]["name"])
            if players[player]["guild"] is None:
                guild = None
            else:
                guild = Guild.objects.get(
                    name=players[player]["guild"]["name"]
                )
            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=race,
                guild=guild,
            )
    pass


if __name__ == "__main__":
    main()
