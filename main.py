from typing import Any
import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def race_func(player: dict) -> Any:
    if not Race.objects.filter(name=player["race"]["name"]).exists():
        race_inst, created = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )
        return race_inst


def skill_func(player: dict) -> None:
    for skill in player["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_func(player)}
            )


def guild_func(player: dict) -> Any:
    guild = player.get("guild")
    if guild is not None:
        if not Guild.objects.filter(name=player["guild"]["name"]).exists():
            guild_inst, created = Guild.objects.get_or_create(
                name=player["guild"]["name"],
                defaults={"description": player["guild"]["description"]}
            )

        else:
            guild_inst = None

        return guild_inst


def player_func(players: dict) -> None:
    for player_name, player in players.items():
        if not Player.objects.filter(nickname=player_name).exists():
            Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=race_func(player),
                guild=guild_func(player)
            )


def main() -> None:

    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player in players.items():
        race_func(player)
        skill_func(player)
        guild_func(player)
        player_func(players)


if __name__ == "__main__":
    main()
