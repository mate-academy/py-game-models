import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for nickname, data in players.items():
        race_data = data["race"]
        guild_data = data["guild"]
        guild = (
            Guild.objects.get(name=guild_data["name"])
            if (guild_data
                and Guild.objects.filter(name=guild_data["name"]).exists())
            else None if not guild_data else
            Guild.objects.create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        )
        race = (
            Race.objects.get(name=race_data["name"])
            if Race.objects.filter(name=race_data["name"]).exists()
            else
            Race.objects.create(
                name=race_data["name"],
                description=race_data["description"]
            )
        )
        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )
        for skill in race_data["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=race_data["name"])
                )


if __name__ == "__main__":
    main()
