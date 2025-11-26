import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for key, value in data.items():
        race_obj, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"])

        guild_obj = None
        if value["guild"] is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"])

        race_obj, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )

        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race_obj)

        Player.objects.get_or_create(nickname=key,
                                     email=value["email"],
                                     bio=value["bio"],
                                     race=race_obj,
                                     guild=guild_obj)


if __name__ == "__main__":
    main()
