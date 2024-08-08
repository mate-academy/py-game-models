import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file_handler:
        loaded_json = json.load(file_handler)

    for nickname, data in loaded_json.items():

        obj, created = Race.objects.get_or_create(
            name=data["race"].get("name"),
            description=data["race"].get("description")
        )

        if data["guild"]:
            obj, created = Guild.objects.get_or_create(
                name=data["guild"].get("name") if data["guild"] else None,
                description=data["guild"].get("description")
            )

        for skill in data["race"]["skills"]:
            obj, created = Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=Race.objects.get(name=data["race"]["name"])
            )

        obj, created = Player.objects.get_or_create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=Race.objects.get(name=data["race"]["name"]),
            guild=(Guild.objects.get(name=data["guild"]["name"])
                   if data["guild"] else None)
        )


if __name__ == "__main__":
    main()
