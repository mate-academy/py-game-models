import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    Player.objects.all().delete()
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, values in players.items():
        guild = values.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=values.get("guild").get("name"),
                description=values.get("guild").get("description")
            )
        race, _ = Race.objects.get_or_create(
            name=values.get("race").get("name"),
            description=values.get("race").get("description")
        )
        for skill in values.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        Player.objects.create(
            nickname=name,
            email=values.get("email"),
            bio=values.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
