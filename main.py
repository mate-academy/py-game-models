import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data = json.load(f)

    for nickname, properties in data.items():
        race_data = properties["race"]
        skills = race_data.pop("skills")

        race = Race.objects.get_or_create(**race_data)[0]

        for skill_data in skills:
            Skill.objects.get_or_create(
                **skill_data,
                race=race,
            )

        guild_data = properties["guild"]
        guild = (
            Guild.objects.get_or_create(**guild_data)[0]
            if guild_data
            else None
        )

        Player.objects.create(
            nickname=nickname,
            email=properties["email"],
            bio=properties["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
