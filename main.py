import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_name, player_data in players.items():
        nickname = player_name
        data = player_data
        name = data["race"]["name"]
        description = data["race"]["description"]
        if not Race.objects.filter(name=name).exists():
            race = Race.objects.create(
                name=name,
                description=description,
            )
        else:
            race = Race.objects.get(name=data["race"]["name"])

        for skill in data["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race,
                )

        if data["guild"]:
            name = data["guild"]["name"]
            description = data["guild"]["description"]
            if not Guild.objects.filter(name=name).exists():
                guild = Guild.objects.create(
                    name=name,
                    description=description,
                )
            else:
                guild = Guild.objects.get(
                    name=name,
                    description=description,
                )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
