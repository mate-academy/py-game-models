import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as f:
        players = json.load(f)

    for player_name, info in players.items():
        race_arguments = info["race"]
        if not Race.objects.filter(name=race_arguments["name"]).exists():
            race = Race.objects.create(
                name=race_arguments["name"],
                description=race_arguments["description"]
            )
        else:
            race = Race.objects.get(name=race_arguments["name"])

        skill_arguments = race_arguments["skills"]
        for skill in skill_arguments:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        guild_arguments = info["guild"]
        if guild_arguments is not None:
            if not Guild.objects.filter(name=guild_arguments["name"]).exists():
                guild = Guild.objects.create(
                    name=guild_arguments["name"],
                    description=guild_arguments["description"]
                )
            else:
                guild = Guild.objects.get(name=guild_arguments["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
