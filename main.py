import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

with open("players.json", "r") as sourse:
    data = json.load(sourse)


def main() -> None:
    for nickname, info in data.items():
        name_race = info["race"]["name"]
        race_description = info["race"]["description"]

        if not Race.objects.filter(name=name_race).exists():
            race = Race.objects.create(
                name=name_race,
                description=race_description
            )
        if info["guild"]:
            guild_name = info["guild"]["name"]
            guild_description = info["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
        else:
            guild = None

        for skill in info["race"]["skills"]:
            name_skill = skill["name"]
            bonus = skill["bonus"]
            if not Skill.objects.filter(name=name_skill).exists():
                Skill.objects.create(
                    name=name_skill,
                    bonus=bonus,
                    race=race
                )

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
