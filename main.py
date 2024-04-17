import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)
    for player_info in players:
        race, _ = Race.objects.get_or_create(
            name=players[player_info]["race"]["name"],
            description=players[player_info]["race"]["description"])
        for skill_info in players[player_info]["race"]["skills"]:
            print()
            skill, _ = Skill.objects.get_or_create(name=skill_info["name"],
                                                   bonus=skill_info["bonus"],
                                                   race=race)
        guild_info = players[player_info].get("guild")

        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_info,
            email=players[player_info]["email"],
            bio=players[player_info]["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
