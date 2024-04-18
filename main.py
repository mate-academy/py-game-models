import json

import init_django_orm  # noqa: F401

from db.models import Race, Guild, Skill, Player


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

        for player_name, player_data in players.items():
            race, _ = Race.objects.get_or_create(
                name=player_data["race"]["name"],
                description=player_data["race"]["description"]
            )
            if player_data.get("guild") is not None:
                guild, _ = Guild.objects.get_or_create(
                    name=player_data["guild"]["name"],
                    description=player_data["guild"]["description"]
                )
            else:
                guild = None

            for skill in player_data["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

            Player.objects.get_or_create(
                nickname=player_name,
                email=player_data["email"],
                bio=player_data["bio"],
                guild_id=guild.id if guild is not None else None,
                race_id=race.id
            )


if __name__ == "__main__":
    main()
