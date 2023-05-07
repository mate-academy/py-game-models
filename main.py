import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for key, value in players_data.items():
        race_info = value["race"]
        race, _ = (
            Race.objects.get_or_create
            (name=race_info.get("name"),
             description=race_info.get("description"))
        )

        for race_skill in value["race"]["skills"]:
            skill, _ = (
                Skill.objects.get_or_create
                (name=race_skill.get("name"),
                 bonus=race_skill.get("bonus"),
                 race=race)
            )

        guild = None
        if value["guild"]:
            guild, _ = (
                Guild.objects.get_or_create
                (name=value["guild"].get("name"),
                 description=value["guild"].get("description"))
            )

        player, _ = Player.objects.get_or_create(nickname=key,
                                                 email=value["email"],
                                                 bio=value["bio"],
                                                 race=race,
                                                 guild=guild)


if __name__ == "__main__":
    main()
