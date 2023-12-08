import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
        for player in players:

            player_race, created = Race.objects.get_or_create(
                name=players[player]["race"]["name"],
                description=players[player]["race"]["description"]
            )

            for skill in players[player]["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

            player_guild = players[player]["guild"] or None
            if player_guild:
                player_guild, created = Guild.objects.get_or_create(
                    name=player_guild["name"],
                    description=player_guild["description"]
                )

            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
