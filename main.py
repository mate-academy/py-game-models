import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for name, data in players.items():
            email = data.get("email")
            bio = data.get("bio")

            race, _ = Race.objects.get_or_create(
                name=data["race"]["name"],
                description=data["race"]["description"],
            )

            for skill in data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

            guild = None
            if data.get("guild"):
                guild, _ = Guild.objects.get_or_create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )

            Player.objects.get_or_create(
                nickname=name,
                email=email,
                bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
