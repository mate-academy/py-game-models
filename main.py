import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for name, data in players.items():
        player = Player(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
        )

        race = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"],
        )
        player.race = race[0]

        for skills in data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=race[0]
            )

        if data.get("guild") is not None:
            guild = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                description=data["guild"]["description"]
            )
            player.guild = guild[0]
        player.save()


if __name__ == "__main__":
    main()
