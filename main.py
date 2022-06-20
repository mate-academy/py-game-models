import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, information in players.items():
        race_name = information["race"]["name"]
        race_description = information["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        skills = information["race"]["skills"]
        for skill in skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=Race.objects.get(name=race_name)
                )

        if information["guild"]:
            guild_name = information["guild"]["name"]
            guild_description = information["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

            Player.objects.create(
                nickname=name,
                email=information["email"],
                bio=information["bio"],
                race=Race.objects.get(name=race_name),
                guild=Guild.objects.get(name=guild_name)
            )
        else:
            Player.objects.create(
                nickname=name,
                email=information["email"],
                bio=information["bio"],
                race=Race.objects.get(name=race_name),
                guild=None
            )


if __name__ == "__main__":
    main()
