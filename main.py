import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for name, values in players.items():
        race, created = Race.objects.get_or_create(
            name=values["race"]["name"],
            description=values["race"]["description"]
        )
        for skill in values["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        guild = values["guild"] if values["guild"] else None
        if guild:
            guild, created = Guild.objects.get_or_create(
                name=values["guild"]["name"],
                description=values["guild"]["description"]
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
