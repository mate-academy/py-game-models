import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_races_and_skills(players: dict) -> None:
    for player_name, player_info in players.items():
        race_info = player_info["race"]
        race, is_race_created = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )
        if is_race_created:
            for skill in race_info["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )


def create_players(players: dict) -> None:
    for player_name, player_info in players.items():
        race = Race.objects.get(name=player_info["race"]["name"])
        guild_info = player_info["guild"]
        guild = None
        if guild_info:
            guild, is_guild_created = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )
        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


def main() -> None:
    with open("players.json") as config_players:
        players: dict = json.load(config_players)

    create_races_and_skills(players)
    create_players(players)


if __name__ == "__main__":
    main()
