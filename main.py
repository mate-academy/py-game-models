import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player, data in players_data.items():
        race, created = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )

        if created:
            skills = [
                Skill(name=skill["name"], bonus=skill["bonus"], race=race)
                for skill in data["race"]["skills"]
            ]
            Skill.objects.bulk_create(skills)

        guild = Guild.objects.get_or_create(
            name=data["guild"]["name"],
            description=data["guild"]["description"]
        )[0] if data["guild"] else None

        Player.objects.create(
            nickname=player,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )
