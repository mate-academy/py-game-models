import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for player in players:
        nickname = player
        email = players[nickname]["email"]
        bio = players[nickname]["bio"]

        # CREATE RACE
        race_info = players[nickname]["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        # CREATE SKILLS
        for skill in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )

        # CREATE GUILD
        if players[nickname]["guild"]:
            guild_info = players[nickname]["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )
        else:
            guild = None

        # CREATE PLAYERS
        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
