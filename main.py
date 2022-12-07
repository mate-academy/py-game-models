import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_dict = json.load(file)

    for nickname, properties in players_dict.items():
        property_race = properties["race"]
        if Race.objects.filter(name=property_race["name"]).exists() is False:
            race = Race.objects.create(
                name=property_race["name"],
                description=property_race["description"]
            )
        else:
            race = Race.objects.get(name=property_race["name"])

        for property_skill in properties["race"]["skills"]:
            if Skill.objects.filter(
                    name=property_skill["name"],
                    race=race
            ).exists() is False:
                Skill.objects.create(
                    name=property_skill["name"],
                    bonus=property_skill["bonus"],
                    race=race
                )

        property_guild = properties["guild"]
        if property_guild is not None:
            if Guild.objects.filter(
                    name=property_guild["name"]
            ).exists() is False:
                guild = Guild.objects.create(
                    name=property_guild["name"],
                    description=property_guild["description"]
                )
            else:
                guild = Guild.objects.get(name=property_guild["name"])
        else:
            guild = None

        if Player.objects.filter(nickname=nickname).exists() is False:
            Player.objects.create(
                nickname=nickname,
                email=properties["email"],
                bio=properties["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
