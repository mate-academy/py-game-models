import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    result_guild = False

    with open("players.json", "r") as file:
        datas = json.load(file)

    for key, data in datas.items():

        r_obj, result = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
        if data["guild"] is not None:
            g_obj, result_guild = Guild.objects.get_or_create(
                name=data["guild"].get("name") ,
                description=data["guild"].get("description")
            )

        Player.objects.get_or_create(
            nickname=key,
            email=data["email"],
            bio=data["bio"],
            race=r_obj,
            guild=g_obj if data["guild"] is not None else None
        )

        if data["race"].get("skills"):
            for skill in data["race"].get("skills"):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=r_obj
                )


if __name__ == "__main__":
    main()
