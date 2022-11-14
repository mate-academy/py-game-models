import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        all_info = json.load(f)

    for key, value in all_info.items():
        race = create_race(value)
        guild = create_guild(value)

        Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild
        )

        create_skills(value)


def create_race(value: dict) -> Race:
    if not Race.objects.filter(name=value["race"]["name"]).exists():
        return Race.objects.create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

    return Race.objects.get(name=value["race"]["name"])


def create_guild(value: dict):
    if value["guild"]:
        if not Guild.objects.filter(
                name=value["guild"]["name"]
        ).exists():
            return Guild.objects.create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )

        return Guild.objects.get(name=value["guild"]["name"])
    return None


def create_skills(value: dict) -> None:
    for skill in value["race"]["skills"]:
        if not Skill.objects.filter(name=skill["name"]).exists():
            Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=create_race(value)
            )


if __name__ == "__main__":
    main()
