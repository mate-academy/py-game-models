import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player_nickname, player_data in players.items():
        race_data = player_data["race"]
        if not Race.objects.filter(name=race_data["name"]).exists():
            Race.objects.create(
                name=race_data["name"],
                description=race_data["description"],
            )
        race = Race.objects.get(name=race_data["name"])

        for skills_data in race_data["skills"]:
            if not Skill.objects.filter(name=skills_data["name"]).exists():
                Skill.objects.create(
                    name=skills_data["name"],
                    bonus=skills_data["bonus"],
                    race=race
                )

        guild_data = player_data["guild"]
        if guild_data:
            if not Guild.objects.filter(name=guild_data["name"]).exists():
                Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
            guild = Guild.objects.get(name=guild_data["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=player_nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
