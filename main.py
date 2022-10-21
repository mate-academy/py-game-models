from json import load

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    pass
    with open("players.json") as file:
        players = load(file)

    for nickname, info in players.items():
        email = info["email"]
        bio = info["bio"]
        race_name = info["race"]["name"]
        race_description = info["race"]["description"]
        race_skills = info["race"]["skills"]
        guild_name = info["guild"]["name"] if info["guild"] else None
        guild_description = (
            info["guild"]["description"]
            if info["guild"] else None
        )

        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        for skill in race_skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=race_name
                )

        if guild_name and not Guild.objects.filter(name=guild_name).exists():
            Guild.objects.create(
                name=guild_name,
                description=guild_description,
            )

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race_id=race_name,
                guild_id=guild_name
            )


if __name__ == "__main__":
    main()
