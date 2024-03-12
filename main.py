import json

import init_django_orm  # noqa: F401
from django.db import IntegrityError
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open(file="players.json", mode="r") as players_file:
        players = json.load(players_file)
    for nickname, options in players.items():
        guild = None
        if options.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=options.get("guild").get("name"),
                description=options.get("guild").get("description"))

        race_options = options.get("race")
        if race_option:
            race, _ = Race.objects.get_or_create(
                name=race_options.get("name"),
                description=race_options.get("description"))

        for skill in race_options.get("skills", []):
            Skill.objects.get_or_create(name=skill.get("name"),
                                        bonus=skill.get("bonus"),
                                        race_id=race.id)

        try:
            Player.objects.create(
                nickname=nickname,
                email=options.get("email"),
                bio=options.get("bio"),
                race=race,
                guild=guild
            )
        except IntegrityError:
            print(f"Player with nickname '{nickname}' already exists.")


if __name__ == "__main__":
    main()
