import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as f:
        players = json.load(f)

    for name, info in players.items():

        user_race = info["race"]
        if not Race.objects.filter(name=user_race["name"]).exists():
            race = Race.objects.create(
                name=user_race["name"],
                description=user_race["description"]
            )
        else:
            race = Race.objects.get(name=user_race["name"])

        for user_skill in user_race["skills"]:
            if not Skill.objects.filter(name=user_skill["name"]).exists():
                Skill.objects.create(
                    name=user_skill["name"],
                    bonus=user_skill["bonus"],
                    race=race
                )

        if info["guild"]:
            user_guild = info["guild"]
            if not Guild.objects.filter(name=user_guild["name"]).exists():
                guild = Guild.objects.create(
                    name=user_guild["name"],
                    description=user_guild["description"]
                )
            else:
                guild = Guild.objects.get(name=user_guild["name"])
        else:
            guild = None

        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
