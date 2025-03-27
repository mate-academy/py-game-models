import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_data = json.load(file)

    for player, data in players_data.items():
        race_data = data["race"]
        if not Race.objects.filter(name=race_data["name"]).exists():
            race = Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )
        else:
            race = Race.objects.get(name=race_data["name"])

        skill_data = race_data["skills"]
        for skill in skill_data:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild_data = data["guild"]
        guild = None
        if guild_data:
            if not Guild.objects.filter(name=guild_data["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_data["name"])

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
