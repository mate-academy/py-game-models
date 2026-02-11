import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for user, value in data.items():
        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"],
        )
        if value["race"]["skills"]:
            for item in value["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=item["name"],
                    bonus=item["bonus"],
                    race=race
                )
        if value["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"],
            )
        else:
            guild = value["guild"]
        Player.objects.get_or_create(
            nickname=user,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
