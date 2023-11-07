import init_django_orm  # noqa: F401
import json
from django.db import models

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:

        data = json.load(players)

        for player_name, player_info in data.items():
            race, created_race = Race.objects.get_or_create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

            for skill in player_info["race"]["skills"]:
                skill, created_skill = Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            guild = None
            if player_info["guild"]:
                guild, created_guild = Guild.objects.get_or_create(
                    name=player_info["guild"]["name"],
                    description=player_info["guild"]["description"],
                )

            Player.objects.create(
                nickname=player_name,
                email=player_info["email"],
                bio=player_info["bio"],
                race=race,
                guild=guild,
                created_at=models.DateTimeField(auto_now_add=True)
            )


if __name__ == "__main__":
    main()
