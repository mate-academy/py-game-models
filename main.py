import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main():
    with open("players.json") as file_read:
        user_data = json.load(file_read)

    for player_name, value in user_data.items():
        if not Race.objects.filter(name=value["race"]["name"]).exists():
            player_race = Race.objects.create(
                name=value["race"]["name"],
                description=value["race"]["description"]
            )
        else:
            player_race = Race.objects.get(
                name=value["race"]["name"]
            )

        for skills in value["race"]["skills"]:
            if not Skill.objects.filter(
                    name=skills["name"]
            ).exists():
                Skill.objects.create(
                    name=skills["name"],
                    bonus=skills["bonus"],
                    race=player_race
                )

        if value["guild"]:
            if not Guild.objects.filter(
                    name=value["guild"]["name"]
            ).exists():
                if value["guild"]["description"]:
                    player_guild = Guild.objects.create(
                        name=value["guild"]["name"],
                        description=value["guild"]["description"]
                    )
                else:
                    player_guild = Guild.objects.create(
                        name=value["guild"]["name"]
                    )
            else:
                player_guild = Guild.objects.get(
                    name=value["guild"]["name"]
                )
        else:
            player_guild = None

        player_email = value["email"]
        player_bio = value["bio"]

        Player.objects.create(
            nickname=player_name,
            email=player_email,
            bio=player_bio,
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
