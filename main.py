import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        data = json.load(f)

        for user, user_data in data.items():
            if not Race.objects.filter(
                    name=user_data["race"]["name"]
            ).exists():
                Race.objects.create(
                    name=user_data["race"]["name"],
                    description=user_data["race"]["description"]
                )

            race = Race.objects.get(name=user_data["race"]["name"])

            for skill in user_data["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

            if user_data["guild"]:
                if not Guild.objects.filter(
                        name=user_data["guild"]["name"]
                ).exists():
                    Guild.objects.create(
                        name=user_data["guild"]["name"],
                        description=user_data["guild"]["description"]
                    )

                    guild = Guild.objects.get(name=user_data["guild"]["name"])

            else:
                guild = None

            if not Player.objects.filter(nickname=user).exists():
                Player.objects.create(
                    nickname=user,
                    email=user_data["email"],
                    bio=user_data["bio"],
                    race=race,
                    guild=guild,
                )


if __name__ == "__main__":
    main()
