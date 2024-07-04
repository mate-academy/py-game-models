import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players = json.load(players_file)
        for player in players:
            race_data = players[player]["race"]
            race, _ = Race.objects.get_or_create(
                name=race_data["name"],
                description=race_data["description"]
            )

            skills_data = race_data["skills"]
            if skills_data:
                for skill in skills_data:
                    Skill.objects.get_or_create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race
                    )

            guild = None
            guild_data = players[player]["guild"]
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    description=guild_data["description"]
                )

            player_data = players[player]
            Player.objects.create(
                nickname=player,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
