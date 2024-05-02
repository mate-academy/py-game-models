import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname in players:
        player_data = players.get(nickname)
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")

        race, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description")
            }
        )

        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name"),
                defaults={
                    "bonus": skill.get("bonus"),
                    "race": race
                }
            )

        if guild_data is not None:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email"),
                "bio": player_data.get("bio"),
                "race": race,
                "guild": guild
            }
        )

    if __name__ == "__main__":
        main()
