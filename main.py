import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for nickname, data in players.items():
        race = data.get("race")
        skills = race.get("skills")
        guild = data.get("guild")

        race = (Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        ))[0]

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        if guild is not None:
            guild = (Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            ))[0]

        Player.objects.get_or_create(
            nickname=nickname,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
