import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

        for player_nickname, player_data in data.items():

            # RACE

            if not Race.objects.filter(
                    name=player_data["race"]["name"]).exists():
                player_race = Race.objects.create(
                    name=player_data["race"]["name"],
                    description=player_data["race"]["description"]
                )
            else:
                player_race = Race.objects.get(
                    name=player_data["race"]["name"])

            # SKILLS

            for skill in player_data["race"]["skills"]:
                if not Skill.objects.filter(name=skill["name"]).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=player_race
                    )

            # GUILD

            if player_data["guild"]:
                if not Guild.objects.filter(
                        name=player_data["guild"]["name"]).exists():
                    player_guild = Guild.objects.create(
                        name=player_data["guild"]["name"],
                        description=player_data["guild"]["description"]
                    )
                else:
                    player_guild = Guild.objects.get(
                        name=player_data["guild"]["name"])
            else:
                player_guild = None

            # PLAYER

            if not Player.objects.filter(nickname=player_nickname).exists():
                Player.objects.create(
                    nickname=player_nickname,
                    email=player_data["email"],
                    bio=player_data["bio"],
                    race=player_race,
                    guild=player_guild
                )


if __name__ == "__main__":
    main()
