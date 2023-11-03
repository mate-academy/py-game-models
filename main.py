import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_data in players.items():
        player_race = player_data.get("race")
        player_guild = player_data.get("guild")

        race, created = Race.objects.get_or_create(
            name=player_race.get("name"),
            description=player_race.get("description")
        )
        if player_guild:
            guild, created = Guild.objects.get_or_create(
                name=player_guild.get("name"),
                description=player_guild.get("description")
            )
        else:
            guild = None

        for skill in player_race["skills"]:
            Skill.objects.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )

        Player.objects.create(
            nickname=player,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
