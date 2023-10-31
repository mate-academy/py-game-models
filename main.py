import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def add_race(player: dict) -> None:
    player_race = player.get("race")
    race_name = player_race.get("name")
    race_description = player_race.get("description")

    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(name=race_name, description=race_description)


def add_skill(player: dict) -> None:
    skills = player["race"]["skills"]
    race_name = player["race"]["name"]

    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=Race.objects.get(name=race_name)
            )


def add_guild(player: dict) -> None:
    guild = player.get("guild")

    if guild:
        guild_name = guild.get("name")
        guild_description = guild.get("description")

        if not Guild.objects.filter(name=guild_name).exists():
            Guild.objects.create(
                name=guild_name,
                description=guild_description
            )


def add_player(player_name: str, players: dict) -> None:
    player = players[player_name]
    race_name = player["race"]["name"]
    guild = player.get("guild")
    guild_name = guild["name"] if guild else None
    Player.objects.create(
        nickname=player_name,
        email=player["email"],
        bio=player["bio"],
        race=Race.objects.get(name=race_name),
        guild=Guild.objects.get(name=guild_name) if guild_name else None
    )


def main() -> None:
    with open("players.json") as players_data:
        players = json.load(players_data)
    for player in players.values():
        add_race(player)
        add_skill(player)
        add_guild(player)

    for player in players:
        add_player(player, players)


if __name__ == "__main__":
    main()
