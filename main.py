import json

from django.core.exceptions import ObjectDoesNotExist
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    dictionary ={
        "skills": [],
        "guild": [],
        "race": []
    }
    for key, value in data.items():
        number_of_skill = 0
        is_race = False
        is_guild = False

        try:
            Race.objects.get(name=data[key]["race"]["name"])
        except ObjectDoesNotExist:
            race = Race.objects.create(
                name=data[key]["race"]["name"],
                description=data[key]["race"]["description"]
            )

        race = Race.objects.get(name=data[key]["race"]["name"])

        for i in data[key]["race"]["skills"]:
            try:
                Skill.objects.get(name=i["name"])
            except ObjectDoesNotExist:
                skill = Skill.objects.create(
                    name=i["name"],
                    bonus=i["bonus"],
                    race=race
                )


        guild_data = data[key]["guild"]
        if guild_data is not None:
            try:
                Guild.objects.get(name=guild_data["name"])
            except ObjectDoesNotExist:
                guild = Guild.objects.create(
                    name=data[key]["guild"]["name"],
                    description=data[key]["guild"]["description"]
                )
        else:
            is_guild = False
        if guild_data is not None:
            guild = Guild.objects.get(name=guild_data["name"])
        else:
            guild = guild_data

        Player.objects.create(
            nickname=key,
            email=data[key]["email"],
            bio=data[key]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
