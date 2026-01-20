import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as f:
        players_info = json.load(f)
    for pl, info in players_info.items():
        race, created = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )
        if created and info["race"]["skills"]:
            for skill in info["race"]["skills"]:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        guild = None
        if info["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )

        Player.objects.create(
            nickname=pl,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    Player.objects.all().delete()
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    main()
