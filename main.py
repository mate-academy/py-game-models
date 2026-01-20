import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        gamers = {}
        guild = Guild
        race = Race
        skill = Skill

        json_data = json.load(json_file)

        for properties in json_data.values():

            race.objects.get_or_create(
                name=properties["race"]["name"],
                description=properties["race"]["description"]
            )

            for skill_data in properties["race"]["skills"]:
                skill.objects.get_or_create(
                    name=skill_data["name"],
                    bonus=skill_data["bonus"],
                    race=race.objects.get(name=properties["race"]["name"])
                )

            if properties["guild"]:
                guild_value = properties["guild"]["name"]
                guild.objects.get_or_create(
                    name=guild_value,
                    description=properties["guild"]["description"])

        for gamer_name, properties in json_data.items():
            gamers[gamer_name] = None
            email = properties["email"]
            bio = properties["bio"]
            guild_object = None

            if properties["guild"]:
                guild_object = guild.objects.get(
                    name=properties["guild"]["name"]
                )

            gamers[gamer_name] = Player.objects.get_or_create(
                nickname=gamer_name,
                email=email,
                bio=bio,
                race=race.objects.get(name=properties["race"]["name"]),
                guild=guild_object
            )


if __name__ == "__main__":
    main()
