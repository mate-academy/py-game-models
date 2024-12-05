import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)
    for name, stats in players.items():
        race = Race.objects.get_or_create(
            name=stats["race"]["name"],
            description=stats["race"]["description"])
        for skill in stats["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race[0])
        if stats["guild"]:
            guild = Guild.objects.get_or_create(
                name=stats["guild"]["name"],
                description=stats["guild"]["description"])
        else:
            guild = None
        Player.objects.create(nickname=name,
                              email=stats["email"],
                              bio=stats["bio"],
                              race=race[0],
                              guild=guild[0] if guild is not None else None)


if __name__ == "__main__":
    main()
