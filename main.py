import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as data:
        players = json.load(data)
    for player in players:

        player_race = players[player].get("race")
        if player_race:
            race = (Race.objects
                    .get_or_create(name=player_race.get("name"),
                                   description=player_race.get("description")))

            for skill in player_race.get("skills", []):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race[0]
                )

        player_guild = players[player].get("guild")
        if player_guild:
            guild = Guild.objects.get_or_create(
                name=player_guild.get("name"),
                description=player_guild.get("description")
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player,
            email=players[player].get("email"),
            bio=players[player].get("bio"),
            race=race[0],
            guild=None if guild is None else guild[0]
        )


if __name__ == "__main__":
    main()
