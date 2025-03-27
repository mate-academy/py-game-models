import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    pass
    with open("players.json", "r") as players_file:
        players = json.load(players_file)

    for player in players:
        race_data = players[player]["race"]
        guild_data = players[player]["guild"]
        skill_data = race_data["skills"]

        player_guild = None
        player_race, is_race_created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )

        if guild_data:
            player_guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )

        if is_race_created:
            for skill in skill_data:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )

        Player.objects.get_or_create(
            nickname=player,
            email=players.get(player)["email"],
            bio=players.get(player)["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
