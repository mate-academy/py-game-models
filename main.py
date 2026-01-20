import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)
    for name, player_data in players_data.items():
        get_or_create_player(name, player_data)


def get_or_create_guild(guild_data: dict) -> Guild:
    guild, created = Guild.objects.get_or_create(
        name=guild_data["name"],
        defaults={"description": guild_data["description"]}
    )
    return guild


def get_or_create_race(race_data: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]}
    )
    return race


def get_or_create_skill(race: Race, skill_data: dict) -> Skill:
    skill, created = Skill.objects.get_or_create(
        name=skill_data["name"],
        defaults={"bonus": skill_data["bonus"], "race": race}
    )
    return skill


def get_or_create_player(name: str, data: dict) -> Player:
    race = get_or_create_race(data["race"])
    guild = get_or_create_guild(data["guild"]) if data["guild"] else None
    for skill_data in data["race"]["skills"]:
        get_or_create_skill(race, skill_data)
    player, created = Player.objects.get_or_create(
        nickname=name,
        defaults={
            "email": data["email"],
            "bio": data["bio"],
            "race": race,
            "guild": guild
        }
    )
    return player


if __name__ == "__main__":
    main()
