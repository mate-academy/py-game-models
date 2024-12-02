import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for name, data in data.items():
        race, _ = Race.objects.get_or_create(
            name=data.get("race").get("name"),
            description=data.get("race").get("description")
        )
        guild = data.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=data.get("guild").get("name"),
                description=data.get("guild").get("description")
            )
        Player.objects.get_or_create(
            nickname=name,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )
        for skill in data.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

if __name__ == "__main__":
    main()
