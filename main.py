import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def get_or_create_skill(name: str, bonus: str, race: Race) -> None:
    Skill.objects.get_or_create(
        name=name,
        defaults={"bonus": bonus, "race": race}
    )


def get_or_create_guild(guild_info: dict) -> Guild | None:
    if not isinstance(guild_info, dict):
        return
    guild, _ = Guild.objects.get_or_create(
        name=guild_info["name"],
        defaults={"description": guild_info["description"]}
    )

    return guild


def get_or_create_race(race_info: dict) -> Race:
    race, _ = Race.objects.get_or_create(
        name=race_info["name"],
        defaults={"description": race_info["description"]}
    )

    for skill in race_info["skills"]:
        get_or_create_skill(skill["name"], skill["bonus"], race)

    return race


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, player_info in players_data.items():
        Player.objects.create(
            nickname=nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=get_or_create_race(player_info["race"]),
            guild=get_or_create_guild(player_info["guild"])
        )


if __name__ == "__main__":
    main()
