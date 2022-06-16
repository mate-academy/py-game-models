import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():

    with open("players.json") as f:
        players_data = json.load(f)

    for nickname, data in players_data.items():
        race_name = data["race"]["name"]
        race_description = data["race"]["description"]
        if not Race.objects.filter(name=race_name).exists():
            if race_description:
                Race.objects.create(
                    name=race_name,
                    description=race_description
                )
            else:
                Race.objects.create(name=race_name)

        race = Race.objects.get(name=race_name)
        skills = data["race"]["skills"]

        if skills:
            for skill in skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

        if data["guild"]:
            guild_name = data["guild"]["name"]
            guild_description = data["guild"]["description"]
            if not Guild.objects.filter(name=guild_name).exists():
                if guild_description:
                    Guild.objects.create(
                        name=guild_name,
                        description=guild_description
                    )
                else:
                    Guild.objects.create(name=guild_name)

        if data["guild"]:
            guild = Guild.objects.get(name=data["guild"]["name"])
            Player.objects.create(
                nickname=nickname,
                email=data["email"],
                bio=data["bio"],
                race=race,
                guild=guild
            )
        else:
            Player.objects.create(
                nickname=nickname,
                email=data["email"],
                bio=data["bio"],
                race=race
            )
    print("done")


if __name__ == "__main__":
    main()
