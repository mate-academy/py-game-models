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


def player_race_check_and_create(race: dict) -> None:
    if not Race.objects.filter(
            name=race["name"]
    ).exists():
        Race.objects.create(
            name=race["name"],
            description=race["description"]
        )
    race_skills_check_and_create(race)
    return Race.objects.get(name=race["name"])


def race_skills_check_and_create(race: dict) -> None:
    for skill in race["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race_id=Race.objects.get(
                    name=race["name"]
                ).id)


def player_guild_check_and_create(guild: dict):
    if guild:
        if not Guild.objects.filter(
                name=guild["name"]
        ).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )
        return Guild.objects.get(name=guild["name"])
    return None


if __name__ == "__main__":
    main()
