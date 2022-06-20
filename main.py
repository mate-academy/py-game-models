import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

BASE_DIR = Path(__file__).resolve().parent


def create_guild(guild: dict):
    if guild:
        guild_name = guild["name"]
        if not Guild.objects.filter(name=guild_name).exists():
            if guild["description"]:
                guild_description = guild["description"]
                Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            else:
                Guild.objects.create(name=guild_name)
        return guild_name
    return None


def create_race(race_name: str, race_description: str):
    if not Race.objects.filter(name=race_name).exists():
        Race.objects.create(
            name=race_name,
            description=race_description
        )
    return race_name


def create_skills(skills: dict, race_name: str):
    race_skills = {
        skill["name"]: skill["bonus"]
        for skill in skills
    }
    for key, value in race_skills.items():
        if not Skill.objects.filter(name=key).exists():
            Skill.objects.create(
                name=key,
                bonus=value,
                race=Race.objects.get(name=race_name)
            )


def create_player(
        nickname: str,
        email: str,
        bio: str,
        guild_name: str,
        race: str
):
    if not Player.objects.filter(nickname=nickname).exists():
        if guild_name:
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=Race.objects.get(name=race),
                guild=Guild.objects.get(name=guild_name)
            )
        else:
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=Race.objects.get(name=race)
            )


def main():
    with open(BASE_DIR / "players.json", "r") as data:
        players = json.load(data)

    for player in players:
        email = players[player]["email"]
        bio = players[player]["bio"]

        guild_name = create_guild(players[player]["guild"])
        race_name = create_race(
            players[player]["race"]["name"],
            players[player]["race"]["description"]
        )
        create_skills(players[player]["race"]["skills"], race_name)
        create_player(
            player,
            email,
            bio,
            guild_name,
            race_name
        )


if __name__ == "__main__":
    main()
