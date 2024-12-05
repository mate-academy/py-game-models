import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)
    for player_nick, player_info in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            description=player_info["race"]["description"])
        for skill_info in player_info["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(name=skill_info["name"],
                                                   bonus=skill_info["bonus"],
                                                   race=race)
        guild_info = player_info.get("guild")

        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=player_nick,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
