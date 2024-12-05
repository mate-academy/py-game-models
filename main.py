import init_django_orm  # noqa: F401
import json


from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for player_name, info in players.items():
        race_inst, _ = Race.objects.get_or_create(
            name=info["race"].get("name"),
            description=info["race"].get("description"),
        )

        for skill in info["race"].get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_inst
            )

        if info["guild"]:
            guild_inst, _ = Guild.objects.get_or_create(
                name=info["guild"].get("name"),
                description=info["guild"].get("description")
            )
        else:
            guild_inst = None

        Player.objects.create(
            nickname=player_name,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_inst,
            guild=guild_inst
        )
