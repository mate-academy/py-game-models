import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        gamers = json.load(file)

    for key, value in gamers.items():
        races = value["race"]
        skills = races["skills"]
        guilds = value["guild"]

        if not Race.objects.filter(name=races["name"]).exists():
            Race.objects.create(
                name=races["name"],
                description=races["description"]
            ),
        race_ = Race.objects.get(name=races["name"])

        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_

                ),
        if guilds:
            if not Guild.objects.filter(name=guilds["name"]).exists():
                Guild.objects.create(
                    name=guilds["name"],
                    description=guilds["description"]
                ),
            guild = Guild.objects.get(name=guilds["name"])
        else:
            guild = None

        if not Player.objects.filter(nickname=key).exists():
            Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=race_,
                guild=guild
            )


if __name__ == "__main__":
    main()
