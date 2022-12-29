import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for name, info in data.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            race = Race.objects.create(name=info["race"]["name"],
                                       description=info["race"]["description"])
        else:
            race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(name=skill["name"],
                                             bonus=skill["bonus"])
            else:
                skill = Skill.objects.get(name=skill["name"])
            skill.race = race
            skill.save()

        if info["guild"] is not None:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
            else:
                guild = Guild.objects.get(name=info["guild"]["name"])
            Player.objects.create(nickname=name, email=info["email"],
                                  bio=info["bio"], race=race, guild=guild)

        else:
            Player.objects.create(nickname=name, email=info["email"],
                                  bio=info["bio"], race=race)


if __name__ == "__main__":
    print(main())
