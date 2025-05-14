import json

from django.core.exceptions import ObjectDoesNotExist
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for key, value in data.items():
        try:
            race = Race.objects.get(name=data[key]["race"]["name"])
        except ObjectDoesNotExist:
            race = Race.objects.create(
                name=data[key]["race"]["name"],
                description=data[key]["race"]["description"]
            )

        for i in data[key]["race"]["skills"]:
            try:
                Skill.objects.get(name=i["name"])
            except ObjectDoesNotExist:
                Skill.objects.create(
                    name=i["name"],
                    bonus=i["bonus"],
                    race=race
                )

        guild_data = data[key]["guild"]
        guild = None
        if guild_data is not None:
            try:
                guild = Guild.objects.get(name=guild_data["name"])
            except ObjectDoesNotExist:
                guild = Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )

        Player.objects.create(
            nickname=key,
            email=data[key]["email"],
            bio=data[key]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
