import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race_info = info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        skills = race_info["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        guild_info = info.get("guild")
        guild = None

        if guild_info:
            guild_info = info["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
