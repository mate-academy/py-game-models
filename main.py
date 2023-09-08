import os
import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
from settings import BASE_DIR


def create_race(race_data: dict) -> Race:
    if Race.objects.filter(name=race_data["name"]).exists():
        return Race.objects.get(name=race_data["name"])
    race = Race.objects.create(
        name=race_data["name"], description=race_data["description"]
    )
    for skill_data in race_data["skills"]:
        Skill.objects.create(
            name=skill_data["name"],
            bonus=skill_data["bonus"],
            race=race,
        )
    return race


def create_guild(guild_data: dict) -> Guild | None:
    if guild_data is None:
        return None
    elif Guild.objects.filter(name=guild_data["name"]).exists():
        return Guild.objects.get(name=guild_data["name"])
    return Guild.objects.create(
        name=guild_data["name"], description=guild_data["description"]
    )


def load_players(filepath: str) -> dict[str, dict]:
    with open(filepath, "r") as fobj:
        players: dict[str, dict] = json.load(fobj)
    return players


def main() -> None:
    players: dict[str, dict] = load_players(
        os.path.join(BASE_DIR, "players.json")
    )

    for nickname, player_data in players.items():
        race_data: dict = player_data["race"]
        guild_data: dict = player_data["guild"]

        race: Race = create_race(race_data)
        guild: Guild | None = create_guild(guild_data)

        Player.objects.create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
