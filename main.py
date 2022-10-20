import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        users = json.load(f)
        for user, information in users.items():
            user_name = user
            user_race = information["race"]
            user_skills = information["race"]["skills"]
            user_guild = information["guild"]

            if not Race.objects.filter(name=user_race["name"]).exists():
                Race.objects.create(
                    name=user_race["name"],
                    description=user_race["description"]
                )

            if user_guild:
                if not Guild.objects.filter(name=user_guild["name"]).exists():
                    Guild.objects.create(
                        name=user_guild["name"],
                        description=user_guild["description"]
                    )
                guild_id = Guild.objects.get(name=user_guild["name"])
            else:
                guild_id = None

            for skill in user_skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=Race.objects.get(name=user_race["name"])
                    )

            Player.objects.create(
                nickname=user_name,
                email=information["email"],
                bio=information["bio"],
                guild=guild_id,
                race=Race.objects.get(name=user_race["name"])
            )


if __name__ == "__main__":
    main()
