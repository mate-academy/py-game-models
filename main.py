import init_django_orm  # noqa: F401
import os
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    path = os.path.join(os.path.dirname(__file__), "players.json")
    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    for k, v in config.items():
        race, _ = Race.objects.get_or_create(
            name=v["race"]["name"],
            description=v["race"]["description"]
        )

        if v.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=v["guild"]["name"],
                description=v["guild"]["description"]
            )
        else:
            guild = None

        for data_skill in v["race"]["skills"]:
            Skill.objects.get_or_create(
                name=data_skill["name"],
                bonus=data_skill["bonus"],
                race=race
            )

        Player.objects.get_or_create(
            nickname=k,
            email=v["email"],
            bio=v["bio"],
            race=race,
            guild=guild
        )

if __name__ == "__main__":
    main()
