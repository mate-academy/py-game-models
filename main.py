import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as json_file:
        players = json.load(json_file)

    for player in players:
        guild, _ = Guild.objects.get_or_create(name=player["guild"])
        race, _ = Race.objects.get_or_create(name=player["race"])
        skill, _ = Skill.objects.get_or_create(name=player["skill"])

        player_obj, _ = Player.objects.get_or_create(nickname=player["nickname"],
                                                     email=player["email"],
                                                     bio=player["bio"],
                                                     race=race,
                                                     guild=guild
                                                     )
    pass


if __name__ == "__main__":
    main()
