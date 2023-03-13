import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():

        race = info.get("race")
        guild = info.get("guild")
        skills = info.get("race").get("skills")

        race, new_race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"],
        )

        if guild:
            guild, new_guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
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
