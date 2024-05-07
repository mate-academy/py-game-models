import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)
    for key, value in players_data.items():
        race = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )
        guild = (None, None)
        if value["guild"]:
            guild = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"],
            )
        for skill in value["race"]["skills"]:
            if skill:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race[0]
                )
            else:
                Skill.objects.get_or_create(
                    name="",
                    bonus="",
                    race=race[0]
                )
        Player.objects.get_or_create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race[0],
            guild=guild[0],
        )


if __name__ == "__main__":
    main()
