from django.db.models import ForeignKey  # noqa: F401
import init_django_orm  # noqa: F401
import json
import datetime
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for name, value in players.items():

        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        guild = None
        if value["guild"] is not None:
            guild, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=(
                    value["guild"]["description"]
                    if value["guild"]["description"]
                    else None
                ),
            )

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        Player.objects.create(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild,
            created_at=datetime.datetime.now(),
        )


if __name__ == "__main__":
    main()
