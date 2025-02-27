import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for key in players.keys():
            Player.objects.get_or_create(nickname=players[key],
                                         email=players[key]["email"],
                                         bio=players[key]["bio"],
                                         race=Race.objects.get_or_create
                                         (players[key]["race"]),
                                         guild_id=Guild.objects.get_or_create
                                         (id=players[key]["guild"])[0],)
            for skill in players[key]["skills"]:
                Skill.objects.get_or_create(name=skill, bonus=skill["bonus"],
                                            race_id=Race.objects.get_or_create
                                            (player=players[key]["race"]),)


if __name__ == "__main__":
    main()
