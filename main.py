import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race_obj, race_was_created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"])
        if race_was_created:
            for skill in info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj)

        guild_obj = None
        if info.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        Player.objects.create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
