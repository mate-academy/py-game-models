import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for person, info in data.items():
        guild_data = info.get("guild")

        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"]
        )

        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        Player.objects.create(
            nickname=person,
            email=info["email"],
            bio=info["bio"],
            guild=guild,
            race=race
        )


if __name__ == "__main__":
    main()
