import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    data_file = "players.json"
    with open(data_file, "r") as work_file:
        work_data = json.load(work_file)

    for player in work_data:

        race_player = Race.objects.get_or_create(
            name=work_data[player]["race"]["name"],
            description=work_data[player]["race"]["description"]
        )[0]

        if work_data[player]["guild"]:
            guild_player = Guild.objects.get_or_create(
                name=work_data[player]["guild"]["name"],
                description=work_data[player]["guild"]["description"]
            )[0]
        else:
            guild_player = None

        Player.objects.get_or_create(
            nickname=player,
            email=work_data[player]["email"],
            bio=work_data[player]["bio"],
            race=race_player,
            guild=guild_player,
        )
        for skill in work_data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_player
            )


if __name__ == "__main__":
    main()
