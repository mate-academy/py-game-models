import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def get_race(race_params: dict) -> Race:
    return Race.objects.get_or_create(
        name=race_params["name"],
        description=race_params["description"],
    )[0]


def get_skill(
        skill_params: dict,
        race: Race
) -> Skill:
    return Skill.objects.get_or_create(
        name=skill_params["name"],
        bonus=skill_params["bonus"],
        race=race
    )[0]


def get_guild(guild_params: dict) -> Guild | None:
    if guild_params:
        return Guild.objects.get_or_create(
            name=guild_params["name"],
            description=guild_params["description"],
        )[0]
    return None


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for player_name in players:

        guild = get_guild(players[player_name]["guild"])

        race = get_race(players[player_name]["race"])

        for skill in players[player_name]["race"]["skills"]:
            get_skill(skill, race)

        Player.objects.create(
            nickname=player_name,
            email=players[player_name]["email"],
            bio=players[player_name]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
