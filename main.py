import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def create_race(race_info: dict[str, list]) -> Race:
    if Race.objects.filter(name=race_info.get("name")).exists():
        race = Race.objects.get(name=race_info.get("name"))
    else:
        race = Race.objects.create(
            name=race_info.get("name"),
            description=race_info.get("description")
        )

    for skills in race_info.get("skills"):
        if not Skill.objects.filter(name=skills.get("name")).exists():
            Skill.objects.create(
                name=skills.get("name"),
                bonus=skills.get("bonus"),
                race=race
            )

    return race


def create_guild(guild_info: None | dict) -> Guild | None:
    if guild_info is None:
        return

    if Guild.objects.filter(name=guild_info.get("name")).exists():
        return Guild.objects.get(name=guild_info.get("name"))

    return Guild.objects.create(
        name=guild_info.get("name"),
        description=guild_info.get("description")
    )


def main() -> None:
    with open("players.json", "r") as file_read_stream:
        players = json.load(file_read_stream)
    for player_name, player_info in players.items():
        race = create_race(player_info.get("race"))
        guild = create_guild(player_info.get("guild"))
        Player.objects.create(
            nickname=player_name,
            email=player_info.get("email"),
            bio=player_info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
