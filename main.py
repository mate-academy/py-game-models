import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        player_list = json.load(file)

    for key, value in player_list.items():
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
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
