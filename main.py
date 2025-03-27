import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for user_name, user_description in data.items():

        race = user_description.get("race")
        if not Race.objects.filter(name=race.get("name")).exists():
            race_instance = Race.objects.create(
                name=race.get("name"),
                description=race.get("description")
            )

        skills = race.get("skills")
        for skill in skills:
            if not Skill.objects.filter(name=skill.get("name")).exists():
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race_instance
                )

        if guild := user_description.get("guild"):
            if not Guild.objects.filter(name=guild.get("name")).exists():
                guild_instance = Guild.objects.create(
                    name=guild.get("name"),
                    description=guild.get("description")
                )
        else:
            guild_instance = None

        if not Player.objects.filter(nickname=user_name).exists():
            Player.objects.create(
                nickname=user_name,
                email=user_description.get("email"),
                bio=user_description.get("bio"),
                race=race_instance,
                guild=guild_instance
            )


if __name__ == "__main__":
    main()
