import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)
        # print(data)

    # create races and guilds
    for player, information in data.items():
        # print(player)

        race = information["race"]
        guild = information["guild"]

        if guild and not Guild.objects.filter(name=guild["name"]).exists():
            Guild.objects.create(
                name=guild["name"],
                description=guild["description"]
            )

        if race and not Race.objects.filter(name=race["name"]).exists():
            Race.objects.create(
                name=race["name"],
                description=race["description"]
            )
            skills = race["skills"]
            for skill in skills:
                if skill and not Skill.objects.filter(
                        name=skill["name"]
                ).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=race["name"])
                    )
        email = information["email"]
        bio = information["bio"]
        race_ref = Race.objects.get(name=race["name"])
        if guild:
            guild_ref = Guild.objects.get(name=guild["name"])
        #
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race_ref,
                guild=guild_ref
            )
        else:
            Player.objects.create(
                nickname=player,
                email=email,
                bio=bio,
                race=race_ref,
            )


if __name__ == "__main__":
    main()
