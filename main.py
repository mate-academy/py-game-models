import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as config_players:
        players = json.load(config_players)

    for player_name, player_info in players.items():
        race = player_info["race"]
        guild = player_info["guild"]

        race, is_race_created = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )

        if is_race_created:
            for skill in player_info["race"]["skills"]:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]

                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )

        if guild:
            guild, is_guild_created = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
