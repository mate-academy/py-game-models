import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        data = json.load(file)

    for nickname, user_data in data.items():

        race = user_data.get("race")
        if race:
            race, _ = Race.objects.get_or_create(
                name=race.get("name"),
                description=race.get("description")
            )

        guild = user_data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        skills = user_data.get("race").get("skills")
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        Player.objects.create(
            nickname=nickname,
            email=user_data.get("email"),
            bio=user_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
