import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    for player, info in players_info.items():
        race = info.get("race")
        guild = info.get("guild")
        skills = info.get("race").get("skills")

        new_race, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        for skill in skills:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=new_race
            )
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        Player.objects.get_or_create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=new_race,
            guild=guild
        )
