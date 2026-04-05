import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data_play = json.load(file)

    for key, value in data_play.items():
        race_obj, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={"description": value["race"].get("description")}
        )
        gild_value = value.get("guild")
        guild_obj = None
        if gild_value:
            guild_obj, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                defaults={"description": value["guild"].get("description")}
            )

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race_obj,
            guild=guild_obj,
        )

        for one_skill in value["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=one_skill["name"],
                race=race_obj,
                defaults={"bonus": one_skill["bonus"]}
            )


if __name__ == "__main__":
    main()
