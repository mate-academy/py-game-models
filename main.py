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

            race_of_user, _ = Race.objects.get_or_create(
                name=user_race["name"],
                description=user_race["description"]
            )

            if user_guild:
                guild_id, _ = Guild.objects.get_or_create(
                    name=user_guild["name"],
                    description=user_guild["description"]
                )
            else:
                guild_id = None

            for skill in user_skills:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_of_user
                    )

            Player.objects.create(
                nickname=user_name,
                email=information["email"],
                bio=information["bio"],
                guild=guild_id,
                race=race_of_user
            )


if __name__ == "__main__":
    main()
