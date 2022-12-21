import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        read_file = json.load(file)
        for key, value in read_file.items():
            if not Race.objects.filter(name=value["race"]["name"]).exists():
                race_instance = Race.objects.create(
                    name=value["race"]["name"],
                    description=value["race"]["description"])
            for i in value["race"]["skills"]:
                if not Skill.objects.filter(name=i["name"]).exists():
                    Skill.objects.create(name=i["name"],
                                         bonus=i["bonus"],
                                         race=race_instance)
            if value["guild"] is not None and \
                    not Guild.objects.filter(
                        name=value["guild"]["name"]).exists():
                guid_instance = Guild.objects.create(
                    name=value["guild"]["name"],
                    description=value["guild"]["description"])
            if value["guild"] is None:
                guid_instance = None
            if not Player.objects.filter(nickname=key).exists():
                Player.objects.create(nickname=key, email=value["email"],
                                      bio=value["bio"], race=race_instance,
                                      guild=guid_instance)


if __name__ == "__main__":
    main()
