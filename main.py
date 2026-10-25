import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    races = {
        (details["race"]["name"], details["race"]["description"])
        for details in players.values()
    }
    [
        Race.objects.get_or_create(name=name, description=description)
        for name, description in races
    ]
    guilds = {
        (details["guild"]["name"], details["guild"]["description"])
        for details in players.values() if details["guild"] is not None
    }
    [
        Guild.objects.get_or_create(name=name, description=description)
        for name, description in guilds
    ]

    for details in players.values():
        for skill in details["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=details["race"]["name"])
            )

    for player, details in players.items():
        Player.objects.get_or_create(
            nickname=player,
            email=details["email"],
            bio=details["bio"],
            race=Race.objects.get(name=details["race"]["name"]),
            guild=None if details["guild"] is None
            else Guild.objects.get(name=details["guild"]["name"]),
        )


if __name__ == "__main__":
    main()
