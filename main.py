import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    pass
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        player_race = player_data["race"]
        player_guild = player_data["guild"]

        get_player_race = create_race(player_race=player_race)
        create_skills(player_race=player_race, race_instance=get_player_race)
        guild = create_guild(player_guild=player_guild)

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data["email"],
            bio=player_data["bio"],
            race=get_player_race,
            guild=guild
        )


def create_race(player_race: dict[str]) -> Race:

    get_player_race, _ = Race.objects.get_or_create(
        name=player_race["name"],
        description=player_race["description"]
    )
    return get_player_race


def create_skills(player_race: dict[str], race_instance: Race) -> None:

    for skill in player_race["skills"]:
        skill, _ = Skill.objects.get_or_create(
            name=skill["name"],
            bonus=skill["bonus"],
            race=race_instance
        )


def create_guild(player_guild: dict[str]) -> Guild | None:
    """
    Creating unique guild name if player has a guild,
    description(not required) and writes guild to DB
    :return: Guild instance
    """
    guild = None
    if player_guild is not None:
        guild, _ = Guild.objects.get_or_create(
            name=player_guild["name"],
            description=player_guild["description"]
        )
    return guild
