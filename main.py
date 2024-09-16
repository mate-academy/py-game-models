import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_config:
        config = json.load(json_config)

    for username, user_data in config.items():

        race = Race.objects.get_or_create(
            name=user_data["race"]["name"],
            description=user_data["race"]["description"]
        )[0]

        [
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
            for skill in user_data["race"]["skills"]
        ]

        guild = Guild.objects.get_or_create(
            name=user_data["guild"]["name"],
            description=user_data["guild"]["description"]
        )[0] if user_data["guild"] else None

        Player.objects.create(
            nickname=username,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
