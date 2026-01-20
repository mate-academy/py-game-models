import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def get_race(race_data: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_data.get("name"),
        description=race_data.get("description")
    )
    return race


def create_skills(skills_data: dict, race: Race) -> None:
    for skill in skills_data:
        skill, _ = Skill.objects.get_or_create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race
        )


def get_guild(guild_data: dict | None) -> Guild | None:
    if not guild_data:
        return
    guild, _ = Guild.objects.get_or_create(
        name=guild_data.get("name"),
        description=guild_data.get("description")
    )
    return guild


def main() -> None:
    pass
    with open("players.json", "r") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        race_data = player_data.get("race")
        race = get_race(race_data)

        create_skills(race_data.get("skills"), race)

        guild = get_guild(player_data.get("guild"))

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
