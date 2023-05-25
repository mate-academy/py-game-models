import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        json_file = json.load(file)

    for player in json_file:
        info = json_file[player]
        race = info.get("race")
        guild = info.get("guild")
        skills = info["race"]["skills"]

        Race.objects.get_or_create(
            name=race.get("name"),
            defaults={"description": race.get("description")}
        )
        race_id = Race.objects.get(name=race.get("name"))

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race_id)

        if guild is not None:
            Guild.objects.get_or_create(
                name=guild.get("name"), defaults={"description": guild.get("description")})

        guild_id = Guild.objects.get(name=guild.get("name")) \
            if guild is not None else None

        Player.objects.get_or_create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race_id,
            guild=guild_id)
