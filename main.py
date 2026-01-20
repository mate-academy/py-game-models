from django.contrib.gis.gdal.geometries.OGRGeometry import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_info = json.load(players_file)
    for player, player_info in players_info.items():
        race = Race.objects.create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"],
        )

    for skill in players_info["race"]["skills"]:
        skill = Skill.objects.create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )
    guild = None
    if player_info.get("guild"):
        guild = Guild.objects.create(
            name=players_info["guilds"]["name"],
            description=players_info["guilds"]["description"],
        )

    Player.objects.create(
        nickname=players_info["players"]["nickname"],
        email=players_info["players"]["email"],
        bio=players_info["players"]["bio"],
        race=players_info["players"]["race"],
        guild=guild
    )


if __name__ == "__main__":
    main()
