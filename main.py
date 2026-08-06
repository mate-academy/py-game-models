import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as source_file:
        data = json.load(source_file)

    for name, info in data.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"], description=info["race"]["description"]
        )
        skills = info.get("race").get("skills")
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    **skill,
                    race=race
                )
        guild = info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(**guild)
        Player.objects.get_or_create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
