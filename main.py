import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for user, info in data.items():
        nickname = user
        email = info.get("email")
        bio = info.get("bio")

        if info["guild"]:
            guild_name = (info["guild"].get("name"))
            guild_description = info["guild"].get("description")

            guild_link, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )
        else:
            guild_link = None

        if info["race"]:
            race_name = info["race"].get("name")
            race_description = info["race"].get("description")

            race_link, _ = Race.objects.get_or_create(
                name=race_name,
                description=race_description
            )

            if info["race"]["skills"]:
                for skill in info["race"]["skills"]:
                    skill_name = skill.get("name")
                    skill_bonus = skill.get("bonus")

                    Skill.objects.get_or_create(
                        name=skill_name,
                        bonus=skill_bonus,
                        race=race_link
                    )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_link,
            guild=guild_link
        )


if __name__ == "__main__":
    main()
