import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_file:
        data = json.load(json_file)

    for name_of_player in data:
        player_data = data[name_of_player]
        guild = player_data.get("guild")

        race, _ = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            defaults={
                "description": player_data["race"]["description"]
            })

        for skill in player_data["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race,
                })

        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"],
                defaults={
                    "description": guild["description"]
                })
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=name_of_player,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            })


if __name__ == "__main__":
    main()
