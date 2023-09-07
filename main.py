import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source:
        config = json.load(source)
    for nickname, info in config.items():
        race_d = info.get("race")
        if Race.objects.filter(name=race_d.get("name")).exists():
            race = Race.objects.get(name=race_d.get("name"))
        else:
            race = Race.objects.create(
                name=race_d.get("name"),
                description=race_d.get("description")
            )
            for skill in race_d.get("skills"):
                if not Skill.objects.filter(name=skill.get("name")).exists():
                    Skill.objects.create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race
                    )
        if info.get("guild"):
            guild_d = info.get("guild")
            if Guild.objects.filter(name=guild_d.get("name")).exists():
                guild = Guild.objects.get(name=guild_d.get("name"))
            else:
                guild = Guild.objects.create(
                    name=guild_d.get("name"),
                    description=guild_d.get("description")
                )
        else:
            guild = None
        if not Player.objects.filter(nickname=nickname).exists:
            Player.objects.create(
                nickname=nickname,
                email=info.get("email"),
                bio=info.get("bio"),
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
