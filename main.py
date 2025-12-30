import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    print(data)
    for name, info in data.items():
        race_info = info.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )

        skills_info = race_info.get("skills")

        for skill in skills_info:
            print(skill)
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )
        guild_info = info.get("guild")
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info.get("name"),
                description=guild_info.get("description")
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": info.get("email"),
                "bio": info.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
