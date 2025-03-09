import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    Player.objects.all().delete()
    with open("players.json", "r") as file:
        players = json.load(file)
        for name, values in players.items():
            guild = None
            if values["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=values["guild"]["name"],
                    description=values["guild"]["description"]
                )
            race, _ = Race.objects.get_or_create(
                name=values["race"]["name"],
                description=values["race"]["description"]
            )
            for skill in values["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            Player.objects.create(
                nickname=name,
                email=values["email"],
                bio=values["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
