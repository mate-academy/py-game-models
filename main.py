import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        file_data: dict = json.load(file)
    for nickname, players_data in file_data.items():
        race_data = players_data["race"]
        guild_data = players_data["guild"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        guild = Guild.objects.get_or_create(
            name=guild_data["name"],
            description=guild_data["description"] if guild_data else None
        )[0] if guild_data else None
        Player.objects.create(
            nickname=nickname,
            email=players_data["email"],
            bio=players_data["bio"],
            race=race,
            guild=guild,
        )
        skills_data = race_data.get("skills")
        if skills_data:
            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
