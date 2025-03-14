import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        reading_file = json.load(file)
        for admin_key, admin_value in reading_file.items():
            race, _ = Race.objects.get_or_create(
                name=admin_value["race"]["name"],
                description=admin_value["race"]["description"]
            )

            if admin_value["guild"]:
                guild, _ = Guild.objects.get_or_create(
                    name=admin_value["guild"]["name"],
                    description=admin_value["guild"]["description"]
                )
            else:
                guild = admin_value["guild"]

            for skills in admin_value["race"]["skills"]:
                Skill.objects.get_or_create(name=skills["name"],
                                            bonus=skills["bonus"],
                                            race=race)

            Player.objects.get_or_create(nickname=admin_key,
                                         email=admin_value["email"],
                                         bio=admin_value["bio"],
                                         race=race,
                                         guild=guild)


if __name__ == "__main__":
    main()
