import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for player_name, data in players.items():
        race_info, _ = Race.objects.get_or_create(
            name=data["race"].get("name"),
            description=data["race"].get("description"),
        )

        for skill in data["race"].get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_info
            )

        if data["guild"]:
            guild_info, _ = Guild.objects.get_or_create(
                name=data["guild"].get("name"),
                description=data["guild"].get("description")
            )
        else:
            guild_info = None

        Player.objects.create(
            nickname=player_name,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race_info,
            guild=guild_info
        )
