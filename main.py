import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player, attributes in data.items():
        name = attributes.get("race").get("name")
        description = attributes.get("race").get("description")
        race = Race.objects.get_or_create(name=name, description=description)
        skills_list = attributes.get("race").get("skills")
        if skills_list:
            for skill in skills_list:
                if not Skill.objects.filter(name=skill.get("name")).exists():
                    Skill.objects.create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=Race.objects.get(name=name)
                    )
        try:
            guild_name = attributes.get("guild").get("name")
            description_guild = attributes.get("guild").get("description")
            guild = Guild.objects.get_or_create(
                name=guild_name,
                description=description_guild
            )
        except AttributeError:
            guild = None

        Player.objects.create(
            nickname=player,
            email=attributes.get("email"),
            bio=attributes.get("bio"),
            race_id=race[0].id,
            guild_id=guild[0].id if guild else None,
        )


if __name__ == "__main__":
    main()
