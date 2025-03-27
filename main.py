from copy import copy

import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        players_dict = json.load(json_file)

    for name, info in players_dict.items():
        race_dict = copy(info["race"])
        del race_dict["skills"]
        race = Race.objects.get_or_create(**race_dict)[0]

        skills = info["race"]["skills"]
        for skill_dict in skills:
            Skill.objects.get_or_create(
                **skill_dict,
                race_id=race.id
            )

        guild_dict = info.get("guild")
        guild_id: int | None = None
        if guild_dict:
            guild_id = Guild.objects.get_or_create(**guild_dict)[0].id

        players_dict = copy(info)
        del players_dict["guild"]
        del players_dict["race"]
        Player.objects.get_or_create(
            nickname=name,
            race_id=race.id,
            guild_id=guild_id,
            **players_dict
        )


if __name__ == "__main__":
    main()
