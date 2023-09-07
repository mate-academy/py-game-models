import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source:
        config = json.load(source)

    for nickname, info in config.items():
        race_d = info.get("race")
        race = Race.objects.get_or_create(
            name=race_d.get("name"),
            description=race_d.get("description")
        )[0]

        for skill in race_d.get("skills"):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        if info.get("guild"):
            guild_d = info.get("guild")
            guild = Guild.objects.get_or_create(
                name=guild_d.get("name"),
                description=guild_d.get("description")
            )[0]
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=nickname,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
