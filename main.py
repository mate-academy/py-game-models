import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

    for nickname, data in data.items():
        race_data = data["race"]
        guild_data = data["guild"]

        race, _ = (
            Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]))

        for skill in race_data["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)

        guild = None
        if guild_data:
            guild, _ = (
                Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]))

        Player.objects.get_or_create(nickname=nickname,
                                     email=data["email"],
                                     bio=data["bio"],
                                     race=race,
                                     guild=guild)


if __name__ == "__main__":
    main()
