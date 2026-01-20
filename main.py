import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        file = json.load(f)
    for key, value in file.items():
        race = Race.objects.get_or_create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race[0]
            )
        guild = [None]
        if value.get("guild") is not None:
            guild = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )


        Player.objects.create(
                nickname=key,
                email=value["email"],
                bio=value["bio"],
                race=race[0],
                guild=guild[0]
            )


if __name__ == "__main__":
    main()
