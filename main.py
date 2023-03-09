import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def create_player(
        nickname: str,
        email: str,
        bio: str,
        race: Race,
        guild: Guild | None
) -> None:
    Player.objects.get_or_create(
        nickname=nickname,
        email=email,
        bio=bio,
        race=race,
        guild=guild
    )


def create_race(race_data: dict) -> Race:
    return Race.objects.get_or_create(
        name=race_data["name"],
        description=race_data["description"]
    )[0]


def create_skills(skills_data: dict, race: Race) -> None:
    if skills_data:
        for skill in skills_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def create_guild(guild_data: dict) -> Guild:
    if guild_data:
        return Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"]
        )[0]


def main() -> None:
    with open("players.json") as file_in:
        game_data = json.load(file_in)

    for player_name, player_data in game_data.items():
        email = player_data["email"]
        bio = player_data["bio"]
        race = player_data["race"]
        skills = race["skills"] if race["skills"] else None
        guild = player_data["guild"] if player_data["guild"] else None

        race = create_race(race)
        create_skills(skills, race)
        guild = create_guild(guild)
        create_player(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
