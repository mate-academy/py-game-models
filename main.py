import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Guild, Player


def main() -> None:

    with open("players.json", "r") as json_list:
        players = json.load(json_list)

    for name in players.keys():
        race_name = players[name]["race"]["name"]
        race_descript = players[name]["race"]["description"]
        Race.objects.get_or_create(
            name=race_name,
            description=race_descript
        )
        race_class = Race.objects.get(name=race_name)
        if players[name]["race"]["skills"]:
            for skill in players[name]["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_class
                )
        if players[name]["guild"] is not None:
            guild_name = players[name]["guild"]["name"]
            guild_descript = players[name]["guild"]["description"]
            Guild.objects.get_or_create(
                name=guild_name,
                description=guild_descript
            )
            guild_class = Guild.objects.get(name=guild_name)
        else:
            guild_class = None

        Player.objects.get_or_create(
            nickname=name,
            email=players[name]["email"],
            bio=players[name]["bio"],
            race=race_class,
            guild=guild_class,
        )


if __name__ == "__main__":
    main()
