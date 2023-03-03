import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        player_data = json.load(file)
        for player, player_data in player_data.items():
            race_data = player_data["race"]
            guild_data = player_data["guild"]

            if Race.objects.filter(
                    name=race_data["name"]
            ).exists():
                race = Race.objects.get(
                    name=race_data["name"]
                )
            else:
                race = Race.objects.create(
                    name=race_data["name"],
                    description=race_data["description"]
                )

            for skill in race_data["skills"]:
                if not Skill.objects.filter(
                        name=skill["name"]
                ).exists():
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

            if player_data["guild"] and Guild.objects.filter(
                    name=guild_data["name"]
            ).exists():
                guild = Guild.objects.get(
                    name=guild_data["name"]
                )
            elif player_data["guild"]:
                guild = Guild.objects.create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )
            else:
                guild = None

            if not Player.objects.filter(nickname=player).exists():
                Player.objects.create(
                    nickname=player,
                    email=player_data["email"],
                    bio=player_data["bio"],
                    guild=guild,
                    race=race
                )


if __name__ == "__main__":
    main()
