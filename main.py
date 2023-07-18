import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name in data:
        player = data[player_name]

        # Define player personal data
        player_data = {
            "nickname": player_name,
            "email": player.get("email"),
            "bio": player.get("bio")
        }

        # Define player race and skills
        race = player.get("race")
        if Race.objects.filter(name=race.get("name")).exists():
            player_data["race"] = Race.objects.get(name=race.get("name"))
        else:
            player_data["race"] = Race.objects.create(
                name=race.get("name"),
                description=race.get("description")
            )
            for skill in race.get("skills"):
                Skill.objects.create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=player_data.get("race")
                )

        # Define player guild
        guild = player["guild"]
        if not guild:
            player_data["guild"] = None
        else:
            if Guild.objects.filter(name=guild.get("name")).exists():
                player_data["guild"] = Guild.objects.get(name=guild["name"])
            else:
                player_data["guild"] = Guild.objects.create(
                    name=guild["name"],
                    description=guild["description"]
                )

        # Create player
        Player.objects.create(**player_data)


if __name__ == "__main__":
    main()
