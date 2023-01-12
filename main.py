import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

with open("players.json", "r") as file_players:
    data = json.load(file_players)


def create_race(player: str) -> None:
    player_race = data[f"{player}"]["race"]
    if not Race.objects.filter(name=player_race["name"]).exists():
        Race.objects.create(
            name=player_race["name"],
            description=player_race["description"]
        )


def create_skill(player: str) -> None:
    race = Race.objects.get(name=data[f"{player}"]["race"]["name"])
    player_skill = data[f"{player}"]["race"]["skills"]
    for skill in player_skill:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def create_guild(player: str) -> None:
    player_guild = data[f"{player}"]["guild"]
    if player_guild:
        if not Guild.objects.filter(name=player_guild["name"]).exists():
            Guild.objects.create(
                name=player_guild["name"],
                description=player_guild["description"]
            )


def create_player(player: str) -> None:
    player_d = data[f"{player}"]
    race = Race.objects.get(name=player_d["race"]["name"])
    guild = (Guild.objects.get(
        name=player_d["guild"]["name"])if player_d["guild"] else None)
    Player.objects.create(
        nickname=player,
        email=player_d["email"],
        bio=player_d["bio"],
        race=race,
        guild=guild
    )


def main() -> None:
    for player in data:
        create_race(player)
        create_skill(player)
        create_guild(player)
        create_player(player)


if __name__ == "__main__":
    main()
