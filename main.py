import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    race_elf = Race.objects.create(
        name=data["john"]["race"]["name"],
        description=data["john"]["race"]["description"]
    )

    race_human = Race.objects.create(
        name=data["andrew"]["race"]["name"],
        description=data["andrew"]["race"]["description"]
    )

    Skill.objects.create(
        name=data["john"]["race"]["skills"][0]["name"],
        bonus=data["john"]["race"]["skills"][0]["bonus"],
        race=race_elf
    )

    Skill.objects.create(
        name=data["john"]["race"]["skills"][1]["name"],
        bonus=data["john"]["race"]["skills"][1]["bonus"],
        race=race_elf
    )

    guild_archers = Guild.objects.create(
        name=data["john"]["guild"]["name"],
        description=(data["john"]["guild"]["description"]
                     if data["john"]["guild"]["description"]
                     else None
                     )
    )

    guild_mags = Guild.objects.create(
        name=data["max"]["guild"]["name"],
        description=(data["max"]["guild"]["description"]
                     if data["max"]["guild"]["description"]
                     else None
                     )
    )

    guild_black_smith = Guild.objects.create(
        name=data["andrew"]["guild"]["name"],
        description=(data["andrew"]["guild"]["description"]
                     if data["andrew"]["guild"]["description"]
                     else None
                     )
    )

    Player.objects.create(
        nickname="john",
        email=data["john"]["email"],
        bio=data["john"]["bio"],
        race=race_elf,
        guild=guild_archers,
    )

    Player.objects.create(
        nickname="max",
        email=data["max"]["email"],
        bio=data["max"]["bio"],
        race=race_elf,
        guild=guild_mags
    )

    Player.objects.create(
        nickname="arthur",
        email=data["arthur"]["email"],
        bio=data["arthur"]["bio"],
        race=race_elf,
        guild=guild_mags
    )

    Player.objects.create(
        nickname="andrew",
        email=data["andrew"]["email"],
        bio=data["andrew"]["bio"],
        race=race_human,
        guild=guild_black_smith
    )

    Player.objects.create(
        nickname="nick",
        email=data["nick"]["email"],
        bio=data["nick"]["bio"],
        race=race_human
    )


if __name__ == "__main__":
    main()
