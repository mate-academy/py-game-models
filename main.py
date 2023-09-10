import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
    for nickname, value in data.items():

        guild = None

        if isinstance(value["guild"], dict):
            guild, created = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

        race, created = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        Player.objects.get_or_create(
            nickname=nickname,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )


if __name__ == "__main__":
    main()
