import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        for key, value in data.items():
            player = Player(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
            )

            race = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
            player.race = race[0]

            for skill in value["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race[0]
                )

            if value["guild"]:
                guild = Guild.objects.get_or_create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"]
                )
                player.guild = guild[0]

            player.save()


if __name__ == "__main__":
    main()
