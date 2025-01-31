import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)

    for dict_name in data:
        Player.objects.get_or_create(
            nickname = dict_name,
            email = dict_name["email"],
            bio = dict_name["bio"]
        )
        Race.objects.get_or_create(
            name = dict_name["race"]["name"],
            description = dict_name["race"]["description"]
        )
        for i in dict_name["race"]["skills"]:
            Skill.objects.get_or_create(
                name = i["name"],
                bonus = i["bonus"]
            )
        Guild.objects.get_or_create(
            name = dict_name["guild"]["name"],
            description = dict_name["guild"]["description"]
        )


if __name__ == "__main__":
    main()
