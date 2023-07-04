import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for key in data:
        race, created = Race.objects.get_or_create(
            name=data[key]["race"]["name"],
            description=data[key]["race"]["description"])

        for skill_name in data[key]["race"]["skills"]:
            if not Skill.objects.filter(name=skill_name["name"]).exists():
                Skill.objects.create(name=skill_name["name"],
                                     bonus=skill_name["bonus"], race=race)
        if data[key]["guild"] is None:
            guild = None
        else:
            guild, created = Guild.objects.get_or_create(
                name=data[key]["guild"]["name"],
                description=data[key]["guild"]["description"])

        if not Player.objects.filter(nickname=key).exists():
            Player.objects.create(nickname=key,
                                  email=data[key]["email"],
                                  bio=data[key]["bio"],
                                  race=race,
                                  guild=guild)


if __name__ == "__main__":
    main()
