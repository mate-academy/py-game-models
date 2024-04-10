import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as file:
        for data in json.load(file).items():
            name, user_data = data
            race_data = user_data["race"]
            user_race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            skills_data = race_data["skills"]
            for skill in skills_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=user_race
                )

            guild_data = user_data["guild"]
            user_guild = None
            if guild_data:
                user_guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"],
                )

            Player.objects.get_or_create(
                nickname=name,
                email=user_data["email"],
                bio=user_data["bio"],
                race=user_race,
                guild=user_guild,
            )


if __name__ == "__main__":
    main()
