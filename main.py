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


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for player_name, player_data in players.items():

        guild = player_data["guild"]
        if guild:
            guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"],
            )[0]

        race = get_race(player_data["race"])

        for skill in player_data["race"]["skills"]:
            get_skill(skill, race)

        Player.objects.create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
