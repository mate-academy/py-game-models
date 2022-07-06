import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as players:
        players = json.load(players)

    for name, data in players.items():
        race_name = data["race"]["name"]
        race_description = data["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        skills = data["race"]["skills"]
        for skill in skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(name=skill_name, bonus=skill_bonus,
                                     race=Race.objects.get(name=race_name))

        if data["guild"]:
            guild_name = data["guild"]["name"]
            guild_description = data["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(name=guild_name,
                                     description=guild_description)

            Player.objects.create(
                nickname=name,
                email=data["email"],
                bio=data["bio"],
                race=Race.objects.get(name=race_name),
                guild=Guild.objects.get(name=guild_name)
            )
        else:
            Player.objects.create(
                nickname=name,
                email=data["email"],
                bio=data["bio"],
                race=Race.objects.get(name=race_name)
            )


if __name__ == "__main__":
    main()
