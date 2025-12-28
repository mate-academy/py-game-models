import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def race_creation(race_data: dict) -> Race:
    race, created = Race.objects.get_or_create(
        name=race_data["name"],
        defaults={"description": race_data["description"]}
    )
    return race


def guild_creation(guild_data: dict) -> Guild | None:
    if guild_data:
        guild, created = Guild.objects.get_or_create(
            name=guild_data["name"],
            defaults={"description": guild_data["description"]}
        )
        return guild
    return None


def skill_creation(skill_data: list, race: Race) -> None:
    if skill_data:
        for skill in skill_data:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


def player_creation(nickname: str,
                    email: str,
                    bio: str,
                    race: Race,
                    guild: Guild) -> None:
    Player.objects.get_or_create(
        nickname=nickname,
        defaults={"email": email,
                  "bio": bio,
                  "race": race,
                  "guild": guild}
    )


def main() -> None:
    with open("players.json", "r") as p:
        players = json.load(p)
    for name, data in players.items():
        race_data = data["race"]
        skill_data = race_data["skills"]
        guild_data = data["guild"]
        race = race_creation(race_data)
        guild = guild_creation(guild_data)
        skill_creation(skill_data, race)
        player_creation(
            name,
            data["email"],
            data["bio"],
            race,
            guild
        )


if __name__ == "__main__":
    main()
