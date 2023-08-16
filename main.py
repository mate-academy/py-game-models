import json

import init_django_orm  # noqa: F401
from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json", "r") as file:
        data: dict = json.load(file)

    for user_name, values in data.items():
        email = values["email"]
        bio = values["bio"]
        race_data = values["race"]
        guild_data = values["guild"]
        skills_data = values["race"]["skills"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        player = Player.objects.create(
            nickname=user_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )

        for skill_data in skills_data:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=player.race
            )


if __name__ == "__main__":
    main()
