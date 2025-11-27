import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    for name, info in players_info.items():
        race_info = info["race"].copy()
        skills_info = race_info.pop("skills")

        race, _ = Race.objects.get_or_create(
            **race_info,
        )

        for skill_ in skills_info:
            Skill.objects.get_or_create(
                race=race,
                **skill_,
            )

        guild = None
        if info.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                **info["guild"]
            )

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
