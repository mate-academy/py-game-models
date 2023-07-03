import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def set_skills(race: Race, race_skills: list[dict]) -> None:
    for skill in race_skills:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def set_guild(guild: dict) -> None:
    if not Guild.objects.filter(name=guild["name"]).exists():
        Guild.objects.create(
            name=guild["name"],
            description=guild["description"]
        )


def main() -> None:
    with open("players.json", "r") as players_data_file:
        players_data = json.load(players_data_file)

    for player_nickname, player_info in players_data.items():
        if not Race.objects.filter(name=player_info["race"]["name"]).exists():
            Race.objects.create(
                name=player_info["race"]["name"],
                description=player_info["race"]["description"]
            )

        race = Race.objects.get(name=player_info["race"]["name"])
        set_skills(race, player_info["race"]["skills"])

        guild = None

        if player_info["guild"]:
            set_guild(player_info["guild"])
            guild = Guild.objects.get(name=player_info["guild"]["name"])

        Player.objects.create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
