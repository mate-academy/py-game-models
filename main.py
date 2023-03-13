import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

with open("players.json", "r") as sourse:
    data = json.load(sourse)


def main() -> None:
    for nickname, info in data.items():
        name_race = info["race"]["name"]
        race_description = info["race"]["description"]
        race, _ = Race.objects.get_or_create(
            name=name_race,
            description=race_description
        )
        guild = None
        if info["guild"]:
            guild_name = info["guild"]["name"]
            guild_description = info["guild"]["description"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        for skill in info["race"]["skills"]:
            name_skill = skill["name"]
            bonus = skill["bonus"]
            Skill.objects.get_or_create(
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
