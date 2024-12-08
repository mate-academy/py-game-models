import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for key, value in players.items():
        check_race = Race.objects.filter(name=value["race"]["name"])
        if not check_race.exists():
            Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
        race = Race.objects.get(name=value["race"]["name"])

        skills = value["race"]["skills"]
        for element in skills:
            check_skill = Skill.objects.filter(name=element["name"])
            if not check_skill.exists():
                Skill.objects.create(
                    name=element["name"],
                    bonus=element["bonus"],
                    race_id=race.id
                )

        guild = None
        if value.get("guild") is not None:
            check_guild = Guild.objects.filter(name=value["guild"]["name"])
            if not check_guild.exists():
                Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )
            guild = Guild.objects.get(name=value["guild"]["name"])

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race_id=race.id,
            guild_id=guild.id if guild else None
        )


if __name__ == "__main__":
    main()
