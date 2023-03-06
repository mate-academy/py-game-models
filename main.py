import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_guild_instance(guild_player_data: dict) -> tuple:
    return Guild.objects.get_or_create(
        name=guild_player_data["name"],
        description=guild_player_data["description"],
    )


def create_race_instance(race_player_data: dict) -> tuple:
    return Race.objects.get_or_create(
        name=race_player_data["name"],
        description=race_player_data["description"],
    )


def create_skills_instances(
        race: Race,
        skills_player_data: list
) -> None:
    if skills_player_data:
        for skill in skills_player_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )


def main() -> None:
    with open("players.json") as file_in:
        players = json.load(file_in)

    for player_name, player_data in players.items():
        guild_player_data = (
            player_data["guild"] if player_data["guild"] else None
        )
        if guild_player_data:
            guild, *_ = create_guild_instance(guild_player_data)

        race_player_data = player_data["race"] if player_data["race"] else None
        if race_player_data:
            race, *_ = create_race_instance(race_player_data)
        skills_player_data = (
            race_player_data["skills"]
            if race_player_data["skills"]
            else None
        )
        create_skills_instances(race, skills_player_data)

        _, created = Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=(guild if guild_player_data else None),
        )
        if not created:
            print(
                f"Player with nickname:{player_name} has been already created!"
            )


if __name__ == "__main__":
    main()
