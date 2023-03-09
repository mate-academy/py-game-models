import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


FILE = "players.json"


def main() -> None:
    with open(FILE, "r") as file:
        players = json.load(file)

    for name, data in players.items():
        race_dict = data["race"]
        if not Race.objects.filter(name=race_dict["name"]).exists():
            Race.objects.create(
                name=race_dict["name"],
                description=race_dict["description"]
            )
        race = Race.objects.get(name=race_dict["name"])

        for skill in race_dict["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"], bonus=skill["bonus"], race=race
                )

        guild = data["guild"] if data["guild"] else None
        if guild:
            if not Guild.objects.filter(name=data["guild"]["name"]).exists():
                Guild.objects.create(
                    name=data["guild"]["name"],
                    description=data["guild"]["description"]
                )
            guild = Guild.objects.get(name=data["guild"]["name"])

        Player.objects.create(
            nickname=name,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
