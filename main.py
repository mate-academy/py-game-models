import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players:
        players_data = json.load(players)
    for player_name in players_data:
        Player.objects.create(
            nickname=player_name,
            email=players_data[player_name]["email"],
            bio=players_data[player_name]["bio"],
            race=player_race_check_and_create(
                players_data[player_name]["race"]
            ),
            guild=player_guild_check_and_create(
                players_data[player_name]["guild"]
            )
        )


def player_race_check_and_create(race: dict) -> Race:
    race_obj, _ = Race.objects.get_or_create(
        name=race["name"],
        description=race["description"]
    )
    race_skills_check_and_create(race)
    return race_obj


def race_skills_check_and_create(race: dict) -> None:
    for skill in race["skills"]:
        _, _ = Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=Race.objects.get(
                name=race["name"]
            ))


def player_guild_check_and_create(guild: dict) -> Guild | None:
    if guild:
        guild, _ = Guild.objects.get_or_create(
            name=guild["name"],
            description=guild["description"]
        )
        return guild
    return None


if __name__ == "__main__":
    main()
