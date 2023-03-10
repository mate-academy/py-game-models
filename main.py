import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


JSON_FILE = "players.json"


def main() -> None:
    with open(JSON_FILE) as f:
        data = json.load(f)
    for player, info in data.items():
        if not Race.objects.filter(name=info["race"]["name"]).exists():
            Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"],
            )

        race = Race.objects.get(name=info["race"]["name"])

        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        guild = info["guild"]
        if guild:
            if not Guild.objects.filter(name=info["guild"]["name"]).exists():
                Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )

            guild = Guild.objects.get(name=info["guild"]["name"])

        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
