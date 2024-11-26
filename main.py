import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_json:
        data_in = json.load(data_json)

    for player, details in data_in.items():
        name = details["race"]["name"]
        description = details["race"]["description"]

        if not Race.objects.filter(name=name).exists():
            Race.objects.create(name=name, description=description)
        race_instance = Race.objects.get(name=name)

        list_of_skills = [
            Skill(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race_instance
            )
            for skill in details["race"]["skills"]
            if not Skill.objects.filter(name=skill["name"]).exists()
        ]
        Skill.objects.bulk_create(list_of_skills)

        if details["guild"]:
            if not Guild.objects.filter(
                    name=details["guild"]["name"]).exists():
                Guild.objects.get_or_create(
                    name=details["guild"]["name"],
                    description=details["guild"]["description"]
                )
            guild = Guild.objects.get(name=details["guild"]["name"])
        else:
            guild = None

        email = details["email"]
        bio = details["bio"]

        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race_instance,
                guild=guild,
            )


if __name__ == "__main__":
    main()
