import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for nickname_, properties in players.items():
        if not Race.objects.all().filter(name=properties["race"]["name"]):
            Race.objects.create(
                name=properties["race"]["name"],
                description=properties["race"]["description"],
            )

        for skill in properties["race"]["skills"]:
            if not Skill.objects.all().filter(name=skill["name"]) and skill:
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=properties["race"]["name"])
                )

        if properties["guild"] and not Guild.objects.all().filter(
                name=properties["guild"]["name"]):
            Guild.objects.create(
                name=properties["guild"]["name"],
                description=properties["guild"]["description"]
            )

        if not properties["guild"]:
            users_guild = None
        else:
            users_guild = Guild.objects.get(name=properties["guild"]["name"])

        Player.objects.create(
            nickname=nickname_,
            email=properties["email"],
            bio=properties["bio"],
            race=Race.objects.get(name=properties["race"]["name"]),
            guild=users_guild
        )


if __name__ == "__main__":
    main()
