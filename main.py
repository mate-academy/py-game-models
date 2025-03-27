import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for nickname, player_data in players_data.items():
        race_data = player_data["race"]
        guild_data = player_data["guild"]
        skills_data = race_data["skills"]

        race_data, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        for skill in skills_data:
            skill = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_data
            )

        if guild_data:
            guild_data, created = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_data,
            guild=guild_data
        )


if __name__ == "__main__":
    main()
