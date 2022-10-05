import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    # read data from file
    with open("players.json") as file:
        players = json.load(file)

    for player, info in players.items():
        guild = None

        # Check for Guild and create if not exist
        if info["guild"]:
            if Guild.objects.filter(name=info["guild"]["name"]).exists():
                guild = Guild.objects.get(name=info["guild"]["name"])
            else:
                guild_description = info["guild"]["description"]
                if not guild_description:
                    guild_description = None

                guild = Guild.objects.create(
                    name=info["guild"]["name"],
                    description=guild_description
                )

        # Check for Race and create if not exist
        if Race.objects.filter(name=info["race"]["name"]).exists():
            race = Race.objects.get(name=info["race"]["name"])
        else:
            race = Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"],
            )

        # Check for Skills and create if not exist
        for skill in info["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                skill = Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        # Create player instance
        Player.objects.create(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


def clear_all_tables():
    Guild.objects.all().delete()
    Skill.objects.all().delete()
    Race.objects.all().delete()
    Player.objects.all().delete()


if __name__ == "__main__":
    clear_all_tables()
    main()
