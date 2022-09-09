import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    Race.objects.all().delete()
    Skill.objects.all().delete()
    Guild.objects.all().delete()
    Player.objects.all().delete()
    with open("players.json", "r") as file_json:
        file_info = json.load(file_json)

        for keys in file_info:
            if not Race.objects.filter(
                    name=file_info[keys]["race"]["name"]).exists():

                Race.objects.create(
                    name=file_info[keys]["race"]["name"],
                    description=file_info[keys]["race"]["description"]
                )
            if file_info[keys]["guild"]:
                if not Guild.objects.filter(
                        name=file_info[keys]["guild"]["name"]).exists():
                    Guild.objects.create(
                        name=file_info[keys]["guild"]["name"],
                        description=file_info[keys]["guild"]["description"]
                    )
            for skill in file_info[keys]["race"]["skills"]:
                if not Skill.objects.filter(
                        name=skill["name"], bonus=skill["bonus"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(
                            name=file_info[keys]["race"]["name"])
                    )
            if file_info[keys]["guild"]:
                Player.objects.create(
                    nickname=keys,
                    email=file_info[keys]["email"],
                    bio=file_info[keys]["bio"],
                    race=Race.objects.get(
                        name=file_info[keys]["race"]["name"]),
                    guild=Guild.objects.get(
                        name=file_info[keys]["guild"]["name"]),
                )
            else:
                Player.objects.create(
                    nickname=keys,
                    email=file_info[keys]["email"],
                    bio=file_info[keys]["bio"],
                    race=Race.objects.get(
                        name=file_info[keys]["race"]["name"]),
                )


if __name__ == "__main__":
    main()
