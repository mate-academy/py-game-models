import json
from django.utils import timezone

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for username, user_data in data.items():
        race = user_data["race"]
        race_char, _ = Race.objects.get_or_create(name=race["name"], description=race["description"])

        skills = race.get("skills", [])
        for skill in skills:
            Skill.objects.get_or_create(name=skill["name"], bonus=skill["bonus"], race=race_char)

        guild = user_data["guild"]
        if guild:
            guild_char, _ = Guild.objects.get_or_create(name=guild["name"], description=guild["description"])
        else:
            guild_char = None

        Player.objects.get_or_create(
            nickname=username,
            email=user_data["email"],
            bio=user_data["bio"],
            race=race_char,
            guild=guild_char,
            created_at=timezone.now(),
        )
    return





if __name__ == "__main__":
    main()
