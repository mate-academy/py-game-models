import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        data = json.load(players_file)

    for nickname, properties in data.items():
        race_data = properties["race"]
        skills = race_data.pop("skills")

        race, _ = Race.objects.get_or_create(**race_data)

        for skill_data in skills:
            Skill.objects.get_or_create(
                **skill_data,
                race=race,
            )

        guild_data = properties["guild"]
        if guild_data:
            guild, _ = Guild.objects.get_or_create(**guild_data)
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=properties["email"],
            bio=properties["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
