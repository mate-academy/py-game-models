import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source_file:
        data = json.load(source_file)

        for nickname, info in data.items():
            race = info["race"]
            skills = race["skills"]
            guild = info["guild"]

            race, created = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            if guild:
                guild, created = Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"]
                )
            Player.objects.create(
                nickname=nickname,
                email=info["email"],
                bio=info["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
