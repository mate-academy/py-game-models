import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def race_and_guild(info, class_name):
    if info is None:
        return None
    elif not class_name.objects.filter(name=info["name"]).exists():
        guild = class_name.objects.create(
            name=info["name"],
            description=info["description"]
        )
        guild.save()
    else:
        guild = class_name.objects.get(name=info["name"])
        guild.save()
    return guild


def main():
    with open("players.json") as json_players:
        players = json.load(json_players)
    for players_name, players_data in players.items():
        race = race_and_guild(players_data["race"], Race)
        for skill in players_data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        Player.objects.create(
            nickname=players_name,
            email=players_data["email"],
            bio=players_data["bio"],
            race=race,
            guild=race_and_guild(players_data["guild"], Guild)
        )


if __name__ == "__main__":
    main()
