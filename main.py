import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name in players:
        player = players[name]

        race = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race_id": race[0].id
                }
            )

        guild = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            defaults={
                "description":
                    player["guild"]["description"]
                    if player["guild"].get("description")
                    else None
            }
        )[0].id if player.get("guild") else None

        Player.objects.get_or_create(
            nickname=name,
            defaults={
                "email": player["email"],
                "bio": player["bio"],
                "race_id": race[0].id,
                "guild_id": guild
            }
        )


if __name__ == "__main__":
    main()
