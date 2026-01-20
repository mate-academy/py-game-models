from typing import Optional

import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def load_players_from_file() -> dict[str, any]:
    with open("players.json", "r") as file:
        players = json.load(file)
    return players


def create_race(race_info: dict[str, any]) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_info["name"],
        description=race_info["description"]
    )
    return race


def create_skills(skills_info: list[dict[str, any]], race: Race) -> None:
    for skill in skills_info:
        Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race
        )


def create_guild(guild_info: Optional[dict[str, any]]) -> Optional[Guild]:
    if guild_info:
        guild, _ = Guild.objects.get_or_create(
            name=guild_info["name"],
            description=guild_info["description"]
        )
    else:
        guild = None
    return guild


def create_player(
        player: str,
        player_info: dict[str, any],
        race: Race,
        guild: Optional[Guild]
) -> None:
    Player.objects.create(
        nickname=player,
        email=player_info["email"],
        bio=player_info["bio"],
        race=race,
        guild=guild,
    )


def main() -> None:
    players = load_players_from_file()

    for player, player_info in players.items():
        race = create_race(player_info.get("race"))
        create_skills(player_info.get("race").get("skills"), race)
        guild = create_guild(player_info.get("guild"))

        create_player(player, player_info, race, guild)


if __name__ == "__main__":
    main()
