from __future__ import annotations
import json
from django.db import IntegrityError, transaction

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "rb") as file:
        users_data = json.load(file)

    for user, info in users_data.items():

        race = get_race(info)

        if info["race"]["skills"]:
            get_skills(info, race)

        guild = get_guild(info)

        try:
            with transaction.atomic():
                Player.objects.create(
                    nickname=user,
                    email=info["email"],
                    bio=info["bio"],
                    race=race,
                    guild=guild
                )
        except IntegrityError:
            pass


def get_race(info: dict) -> Race:

    try:
        with transaction.atomic():
            return Race.objects.create(
                name=info["race"]["name"],
                description=info["race"]["description"]
            )
    except IntegrityError:
        return Race.objects.get(name=info["race"]["name"])


def get_skills(info: dict, race: Race) -> None:
    for skill in info["race"]["skills"]:
        try:
            with transaction.atomic():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )
        except IntegrityError:
            pass


def get_guild(info: dict) -> Guild | None:
    if info["guild"]:
        try:
            with transaction.atomic():
                return Guild.objects.create(
                    name=info["guild"]["name"],
                    description=info["guild"]["description"]
                )
        except IntegrityError:
            return Guild.objects.get(name=info["guild"]["name"])


if __name__ == "__main__":
    main()
