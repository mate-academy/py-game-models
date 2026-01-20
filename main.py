import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        data: dict = json.load(f)

    for nickname, user_info in data.items():

        race, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"]
        )

        for skill in user_info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        if user_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=user_info["guild"]["name"],
                description=user_info["guild"]["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=nickname,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
