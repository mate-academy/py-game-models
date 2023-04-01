import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_or_create_race(player_data: dict) -> Race:
    race_data = player_data.get("race")
    race_name = race_data.get("name")
    race_description = race_data.get("description")

    race, created = Race.objects.get_or_create(
        name=race_name,
        description=race_description
    )

    return race


def get_or_create_guild(player_data: dict) -> Guild:
    guild_data = player_data.get("guild")
    guild = None

    if guild_data:
        guild_name = guild_data.get("name")
        guild_description = guild_data.get("description")

        guild, created = Guild.objects.get_or_create(
            name=guild_name,
            description=guild_description
        )

    return guild


def create_race_skills(player_data: dict) -> None:
    race_data = player_data.get("race")
    race_name = race_data.get("name")
    race_skills = race_data.get("skills")

    for skill in race_skills:
        skill_name = skill.get("name")
        skill_bonus = skill.get("bonus")
        skill_race = Race.objects.get(name=race_name)

        Skill.objects.get_or_create(
            name=skill_name,
            bonus=skill_bonus,
            race=skill_race
        )


def create_player(player_name: str, player_data: dict, race: Race, guild: Guild) -> None:
    nickname = player_name
    email = player_data.get("email")
    bio = player_data.get("bio")

    Player.objects.create(
        nickname=nickname,
        email=email,
        bio=bio,
        race=race,
        guild=guild
    )


def main() -> None:
    with open("players.json") as source_file:
        players = json.load(source_file)

    for player in players.items():
        (player_name, player_data) = player

        race = get_or_create_race(player_data)
        guild = get_or_create_guild(player_data)
        create_race_skills(player_data)
        create_player(player_name, player_data, race, guild)


if __name__ == "__main__":
    main()
