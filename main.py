import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for nickname, value in players.items():
            race = value["race"]
            new_race, _ = Race.objects.get_or_create(
                name=race["name"],
                description=race["description"]
            )

            skills = race["skills"]
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=new_race
                )

            guild = value["guild"]
            if guild:
                new_guild, _ = Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"]
                )
            else:
                new_guild = None

            Player.objects.create(
                nickname=nickname,
                email=value["email"],
                bio=value["bio"],
                race=new_race,
                guild=new_guild
            )


if __name__ == "__main__":
    main()
