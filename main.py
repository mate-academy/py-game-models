import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def fill_race(person):
    race_name = person["race"]["name"]
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name,
                            description=person["race"]["description"])

    return Race.objects.get(name=race_name)


def fill_skill(skill, person):
    if not Skill.objects.filter(name=skill["name"]).exists():
        Skill.objects.create(**skill, race=fill_race(person))


def fill_guild(person):
    if person["guild"]:
        guild_name = person["guild"]["name"]
        if not Guild.objects.filter(name=guild_name).exists():
            Guild.objects.create(**person["guild"])
        return Guild.objects.get(name=guild_name)
    return None


def main():
    with open("players.json") as source_file:
        data = json.load(source_file)
    for person in data:
        Player.objects.create(
               nickname=person,
               email=data[person]["email"],
               bio=data[person]["bio"],
               race=fill_race(data[person]),
               guild=fill_guild(data[person]),
               )
        for skill in data[person]["race"]["skills"]:
            fill_skill(skill, data[person])


if __name__ == "__main__":
    main()
