import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_data = json.load(players_file)

    for name, player in players_data.items():
        race = player["race"]
        race_obj, created = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        if created:
            for skill in race["skills"]:

                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_obj
                )

        guild = player["guild"]
        if guild:

            guild, created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )

        Player.objects.get_or_create(
            nickname=name,
            email=player["email"],
            bio=player["bio"],
            race=race_obj,
            guild=guild
        )
