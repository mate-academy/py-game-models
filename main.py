import json

import init_django_orm  # noqa: F401

from db.models import Player, Race, Guild, Skill  # noqa: F401


def main() -> None:
    with open("players.json") as data:
        users_data = json.load(data)

        for nickname, other_data in users_data.items():
            race_data = other_data["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )
            guild_data = other_data["guild"]
            skills_list = race_data["skills"]
            for skill in skills_list:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
            if guild_data:
                guild_data, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )

            Player.objects.create(
                nickname=nickname,
                email=other_data["email"],
                bio=other_data["bio"],
                race=race,
                guild=guild_data,
            )


if __name__ == "__main__":
    main()
