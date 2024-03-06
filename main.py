import json


import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for nickname, options in data.items():
        guild = None
        if options.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=options.get("guild").get("name"),
                description=options.get("guild").get("description"),
            )

        race, _ = Race.objects.get_or_create(
            name=options.get("race").get("name"),
            description=options.get("race").get("description"),
        )

        for skill in options.get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race_id=race.id,
            )

        Player.objects.create(
            nickname=nickname,
            email=options.get("email"),
            bio=options.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
