import init_django_orm  # noqa: F401
import json
from django.db import models

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:

        data = json.load(players)

        for key, item in data.items():
            race, created_race = Race.objects.get_or_create(
                name=item["race"]["name"],
                description=item["race"]["description"]
            )

            for skill in item["race"]["skills"]:
                skill, created_skill = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild = None
            if item["guild"]:
                guild, created_guild = Guild.objects.get_or_create(
                    name=item["guild"]["name"],
                    description=item["guild"]["description"],
                )

            Player.objects.create(
                nickname=key,
                email=item["email"],
                bio=item["bio"],
                race=race,
                guild=guild,
                created_at=models.DateTimeField(auto_now_add=True)
            )


if __name__ == "__main__":
    main()
