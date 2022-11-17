import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as players:
        data = json.load(players)
        list_race = []
        for name, info in data.items():
            if info["race"]["name"] not in list_race:
                list_race.append(info["race"]["name"])
                Race.objects.create(
                    name=info["race"]["name"],
                    description=info["race"]["description"]
                )

        skills = list(data.values())[1]["race"]["skills"]
        for skill in skills:
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name="elf")
            )

        list_guils = []
        for name, info in data.items():
            if isinstance(info["guild"], dict) and\
                    info["guild"]["name"] not in list_guils:
                list_guils.append(info["guild"]["name"])
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
        for name, info in data.items():
            if info["guild"] is not None:
                Player.objects.create(
                    nickname=name,
                    email=info["email"],
                    bio=info["bio"],
                    race=Race.objects.get(name=info["race"]["name"]),
                    guild=Guild.objects.get(name=info["guild"]["name"])
                )
            else:
                Player.objects.create(
                    nickname=name,
                    email=info["email"],
                    bio=info["bio"],
                    race=Race.objects.get(name=info["race"]["name"])
                )
