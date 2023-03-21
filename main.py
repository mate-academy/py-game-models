import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


with open("players.json") as players:
    players_data = json.load(players)


def main() -> None:
    for name, data in players_data.items():

        if not Race.objects.filter(name=data["race"]["name"]).exists():
            race = Race.objects.create(
                name=data["race"]["name"],
                description=data["race"]["description"]
            )
        else:
            race = Race.objects.get(name=data["race"]["name"])

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"]
                )
            else:
                skill = Skill.objects.get(name=skill["name"])
            skill.race = race
            skill.save()

        guild = None
        if data["guild"] is not None:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=data["guild"]["name"])

        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
