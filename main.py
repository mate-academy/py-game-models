import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
from django.utils.timezone import now


def main() -> None:
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Player.objects.all().delete()
    Guild.objects.all().delete()

    with open("players.json") as file:
        players = json.load(file)

    for key, player in players.items():
        race, created = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"].get("description", "")}
        )

        if player["guild"]:
            guild, created = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={
                    "description": player["guild"].get("description", "")
                }
            )

        if player["race"]["skills"]:
            for skill in player["race"]["skills"]:

                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=key,
            email=player["email"],
            bio=player["bio"],
            race=race,
            guild=guild if player["guild"] else None,
            created_at=now()
        )
