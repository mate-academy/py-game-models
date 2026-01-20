import json

import init_django_orm  # noqa: F401
from django.db import transaction
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)
    for player_data in players_data:
        with transaction.atomic():
            race_data = players_data[player_data]["race"]
            race = Race.objects.get_or_create(
                name=race_data["name"],
                defaults={"description": race_data.get("description", "")})[0]
            skills = race_data.get("skills", [])
            for skill_data in skills:
                Skill.objects.get_or_create(name=skill_data["name"],
                                            race=race,
                                            defaults={"bonus": skill_data.
                                            get("bonus", 0)})

            guild_data = players_data[player_data].get("guild")
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description", "")}
                )

            Player.objects.get_or_create(
                nickname=player_data,
                defaults={
                    "email": players_data[player_data].get("email", ""),
                    "bio": players_data[player_data].get("bio", ""),
                    "race": race,
                    "guild": guild,
                }
            )


if __name__ == "__main__":
    main()
