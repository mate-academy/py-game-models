import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.loads(file.read())

    for player, info in players_info.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            defaults={"description": info["race"]["description"]}
        )

        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race}
            )

        guild = None
        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                defaults={"description": info["guild"]["description"]}
            )

        Player.objects.get_or_create(
            nickname=player,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild
            }
        )
