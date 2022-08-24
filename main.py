import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main():
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    with open("players.json") as data_file:
        players_data = json.load(data_file)
    for key, value in players_data.items():
        if not Race.objects.filter(
                name=value["race"]["name"]).exists():
            Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
        for skill in value["race"]["skills"]:
            if len(skill) > 0 and \
                    not Skill.objects.filter(
                        name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=value["race"]["name"])
                )
        if value["guild"] is not None:
            if not Guild.objects.filter(
                    name=value["guild"]["name"]).exists():
                Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )
            guild_value = Guild.objects.get(name=value["guild"]["name"])
        else:
            guild_value = None
        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=Race.objects.get(name=value["race"]["name"]),
            guild=guild_value
        )


if __name__ == '__main__':
    main()
