import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
from django.shortcuts import get_object_or_404
from django.http.response import Http404


def create_race(race_info: dict[str, list]) -> Race:
    try:
        racer_name = race_info.get("name")
        race = get_object_or_404(Race, name=racer_name)
    except Http404:
        race = Race.objects.create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )

    for skills in race_info.get("skills"):
        try:
            skill_name = skills.get("name")
            get_object_or_404(Skill, name=skill_name)
        except Http404:
            Skill.objects.create(
                name=skills.get("name"),
                bonus=skills.get("bonus"),
                race=race
            )

    return race


def create_guild(guild_info: None | dict) -> Guild | None:
    if guild_info is None:
        return
    try:
        guild_name = guild_info.get("name")
        return get_object_or_404(Guild, name=guild_name)
    except Http404:
        return Guild.objects.create(
            name=guild_info.get("name"),
            description=guild_info.get("description")
        )


def main() -> None:
    with open("players.json", "r") as file_read_stream:
        players = json.load(file_read_stream)
    for player_name, player_info in players.items():
        race = create_race(player_info.get("race"))
        guild = create_guild(player_info.get("guild"))
        Player.objects.create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
