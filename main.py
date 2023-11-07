import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, info in data.items():
        race_data = info["race"]
        guild_data = info.get("guild")
        skills = race_data["skills"]

        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )
        else:
            guild = None

        for skill in skills:
            skill, created = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
