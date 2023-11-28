import init_django_orm  # noqa: F401
import json
#final solution
from db.models import Race, Skill, Player, Guild


def race_func(race_data: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_data.get("name"),
        description=race_data.get("description")
    )
    return race


def guild_func(guild_data: dict) -> Guild | None:
    guild = None
    if guild_data:
        guild, created = Guild.objects.get_or_create(
            name=guild_data.get("name"),
            description=guild_data.get("description")
        )
    return guild


def skill_func(skills_data: dict, race: dict) -> None:
    for skill in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race
        )


def player_func(player_name: dict,
                player_data: dict,
                race: dict,
                guild: dict) -> None:
    player, created = Player.objects.get_or_create(
        nickname=player_name,
        email=player_data.get("email"),
        bio=player_data.get("bio"),
        race=race,
        guild=guild
    )
    return player


def data_func(file_data: dict) -> tuple:
    race_data = file_data.get("race")
    skill_data = race_data.get("skills")
    guild_data = file_data.get("guild")
    return race_data, skill_data, guild_data


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for player_name, player_data in data.items():
        race_data, skill_data, guild_data = data_func(player_data)
        race = race_func(race_data)
        guild = guild_func(guild_data)
        skill_func(skill_data, race)
        player_func(player_name, player_data, race, guild)


if __name__ == "__main__":
    main()
