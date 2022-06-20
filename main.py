import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_race_field(data):
    if not Race.objects.filter(name=data["race"]["name"]).exists():
        Race.objects.create(
            name=data["race"]["name"],
            description=data["race"]["description"],
        )
    return Race.objects.get(name=data["race"]["name"])


def get_guild_field(data):
    if data["guild"]:
        if not Guild.objects.filter(name=data["guild"]["name"]).exists():
            Guild.objects.create(
                name=data["guild"]["name"],
                description=data["guild"]["description"],
            )
        return Guild.objects.get(name=data["guild"]["name"])


def get_skills_field(data):
    for skill in data["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=data["race"]["name"])
            )


def main():
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, data in players.items():
        race = get_race_field(data)
        guild = get_guild_field(data)
        get_skills_field(data)

        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
