import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for player in players:
        player_info = players[player]
        player_race = player_info["race"]
        player_guild = player_info["guild"]

        player_race_id = create_race_with_skills(player_race)
        player_guild_id = create_guild(player_guild)

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=player_info["email"],
                bio=player_info["bio"],
                race_id=player_race_id,
                guild_id=player_guild_id,
            )


def create_race_with_skills(race: dict) -> int:
    if not Race.objects.filter(name=race["name"]).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )
    race_id = Race.objects.get(name=race["name"]).id

    skills = race["skills"]
    for skill in skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=race_id
            )

    return race_id


def create_guild(guild: dict) -> int | None:
    if not guild:
        return None

    if not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )
    guild_id = Guild.objects.get(name=guild["name"]).id
    return guild_id


if __name__ == "__main__":
    main()
