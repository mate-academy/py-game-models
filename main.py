import json
from pathlib import Path

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

BASE_DIR = Path(__file__).resolve().parent


def main():
    with open(BASE_DIR / "players.json", "r") as data:
        players = json.load(data)

    for player in players:
        email = players[player]["email"]
        bio = players[player]["bio"]
        race_name = players[player]["race"]["name"]
        race_description = players[player]["race"]["description"]
        race_skills = {
            skill["name"]: skill["bonus"]
            for skill in players[player]["race"]["skills"]
        }
        guild = players[player]["guild"]

        if guild:
            guild_name = guild["name"]
            if not Guild.objects.filter(name=guild_name).exists():
                if guild["description"]:
                    guild_description = guild["description"]
                    Guild.objects.create(
                        name=guild_name,
                        description=guild_description
                    )
                else:
                    Guild.objects.create(name=guild_name)

        if not Race.objects.filter(name=race_name).exists():
            Race.objects.create(
                name=race_name,
                description=race_description
            )

        for key, value in race_skills.items():
            if not Skill.objects.filter(name=key).exists():
                Skill.objects.create(
                    name=key,
                    bonus=value,
                    race=Race.objects.get(name=race_name)
                )
        if not Player.objects.filter(nickname=player).exists():
            if guild:
                Player.objects.create(
                    nickname=player,
                    email=email,
                    bio=bio,
                    race=Race.objects.get(name=race_name),
                    guild=Guild.objects.get(name=guild_name)
                )
            else:
                Player.objects.create(
                    nickname=player,
                    email=email,
                    bio=bio,
                    race=Race.objects.get(name=race_name)
                )


if __name__ == "__main__":
    main()
