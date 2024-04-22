import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    Player.objects.all().delete()

    for name, player in players_data.items():
        Race.objects.get_or_create(name=player["race"]["name"],
                                   description=player["race"]["description"])  # noqa
        if player["guild"]:
            Guild.objects.get_or_create(name=player["guild"]["name"],
                                        description=player["guild"]["description"])  # noqa

        race = Race.objects.get(name=player["race"]["name"])
        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)

        guild = Guild.objects.get(name=player["guild"]["name"]) \
            if player["guild"] else None
        Player.objects.create(nickname=name,
                              email=player["email"],
                              bio=player["bio"],
                              race=race,
                              guild=guild)


if __name__ == "__main__":
    main()
