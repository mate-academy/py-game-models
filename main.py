import json
from typing import List

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def read_from_json(data_file: str):
    with open(data_file, "r") as work_file:
        work_data = json.load(work_file)

    for player in work_data:

        ttt = 0

        race_player = Race.objects.get_or_create(
            name=work_data[player]["race"]["name"],
            description=work_data[player]["race"]["description"]
        )

        # uuuu = race_player[0].id
        # uu_uu = Race.objects.get(name=work_data[player]["race"]["name"]).id

        guild_player = Guild.objects.get_or_create(
            name=work_data[player]["guild"]["name"],
            description=work_data[player]["guild"]["description"]
        )

        Player.objects.get_or_create(
            nickname=player,
            email=work_data[player]["email"],
            bio=work_data[player]["bio"],
            race=race_player,
            guild=guild_player
        )
        for skill in work_data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill.name,
                bonus=skill.bonus,
                race=Race.objects.filter(name=work_data[player]["race"]["name"])
            )
    return False


def main() -> None:
    data_file = "players.json"
    work_data_player = read_from_json(data_file)

    mmm = 0


if __name__ == "__main__":
    main()
