import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json", "r") as json_file:
        players = json.load(json_file)
    for player_name, player in players.items():
        if not Race.objects.filter(name=f"{player['race']['name']}").exists():
            Race.objects.create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            )

        for skill in player["race"]["skills"]:
            if not Skill.objects.filter(name=f"{skill['name']}").exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=Race.objects.get(name=player["race"]["name"])
                )

        if player['guild']:
            if not Guild.objects.filter(
                    name=f"{player['guild']['name']}"
            ).exists():
                Guild.objects.create(
                    name=player["guild"]["name"],
                    description=player["guild"]["description"]
                )
            Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=Race.objects.get(name=player["race"]["name"]),
                guild=Guild.objects.get(name=player["guild"]["name"])
            )
        else:
            Player.objects.create(
                nickname=player_name,
                email=player["email"],
                bio=player["bio"],
                race=Race.objects.get(name=player["race"]["name"]),
            )


if __name__ == "__main__":
    main()
