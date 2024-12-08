import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()

    with open("players.json", "r") as file:
        players = json.load(file)

    for key, value in players.items():
        race, created = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults={
                "name": value["race"]["name"],
                "description": value["race"]["description"]
            }
        )

        skills = value["race"]["skills"]
        for element in skills:
            Skill.objects.get_or_create(
                name=element["name"],
                defaults={
                    "name": element["name"],
                    "bonus": element["bonus"],
                    "race_id": race.id
                }
            )

        guild = None
        if value.get("guild") is not None:
            guild, created = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                defaults={
                    "name": value["guild"]["name"],
                    "description": value["guild"]["description"]
                }
            )

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race_id=race.id,
            guild_id=guild.id if guild else None
        )


if __name__ == "__main__":
    main()
