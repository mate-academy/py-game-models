import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player, info in data.items():
        race = info.get("race")
        skills = race.get("skills", [])
        race, _ = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )
        for skill in skills:
            Skill.objects.get_or_create(
                race=race,
                **skill
            )
        guild = info.get("guild")
        if guild is not None:
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        Player.objects.create(
            nickname=player,
            email=info.get("email"),
            bio=info.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
