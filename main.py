import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for name, info in data.items():
        race_name = info["race"]["name"]
        race_description = info["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(name=race_name,
                                description=race_description)

        skills = info["race"]["skills"]
        for skill in skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(name=skill_name,
                                     bonus=skill_bonus,
                                     race=Race.objects.get(name=race_name))

        if not info["guild"]:
            guild_obj = None
        else:
            guild_name = info["guild"]["name"]
            guild_description = info["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                Guild.objects.create(name=guild_name,
                                     description=guild_description)
            guild_obj = Guild.objects.get(name=guild_name)

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=race_name),
            guild=guild_obj)
