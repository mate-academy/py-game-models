import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players:
        data = json.load(players)

    for player in data:
        race_add, _ = Race.objects.get_or_create(
            name=data[player]["race"]["name"],
            description=data[player]["race"]["description"],
        )

        for skill in data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_add,
            )

        guild = data[player].get("guild", None)
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"],
            )

        Player.objects.get_or_create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=race_add,
            guild=guild,
        )
