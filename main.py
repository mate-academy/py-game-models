import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for name, info in players.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"])
        if (info["guild"] is not None and not
                Guild.objects.filter(name=info["guild"]["name"]).exists()):
            Guild.objects.create(
                name=info["guild"]["name"],
                description=info["guild"]["description"])
        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=info["race"]["name"]))
        player_guild = (None if info["guild"] is None
                        else Guild.objects.get(name=info["guild"]["name"]))
        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=Race.objects.get(name=info["race"]["name"]),
            guild=player_guild
        )


if __name__ == "__main__":
    main()
