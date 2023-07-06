import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_skill(race: dict) -> None:
    skills = race["skills"]
    if skills:
        for skill in skills:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(name=skill["name"],
                                     bonus=skill["bonus"],
                                     race_id=Race.objects.get(
                                         name=race["name"]).id)


def create_race(players_data: dict, user: dict) -> dict:
    race = players_data[user].get("race")
    if race and not Race.objects.filter(name=race["name"]).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )
        create_skill(race)
    return race


def create_guild(players_data: dict, user: dict) -> int:
    guild = players_data[user].get("guild")
    if guild:
        guild_obj, created = Guild.objects.get_or_create(
            name=guild["name"],
            defaults={"description": guild["description"]}
        )
        guild_id = guild_obj.id
    else:
        guild_id = guild
    return guild_id


def create_player(
        user: dict,
        players_data: dict,
        race: dict,
        guild_id: int
) -> None:
    Player.objects.create(
        nickname=user,
        email=players_data[user].get("email"),
        bio=players_data[user].get("bio"),
        race_id=Race.objects.get(name=race["name"]).id,
        guild_id=guild_id
    )


def main() -> None:
    with open("players.json", "r") as source:
        players_data = json.load(source)

    for user in players_data:
        race = create_race(players_data, user)

        guild_id = create_guild(players_data, user)

        create_player(user, players_data, race, guild_id)
