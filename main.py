import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name, value in players.items():
        race = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"])[0]

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race,
                }
            )

        guild = None if not value["guild"] else Guild.objects.get_or_create(
            name=value["guild"]["name"],
            description=value["guild"]["description"]
        )[0]

        Player.objects.create(
            nickname=name,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
