import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        player_race = player_data.get("race")
        player_guild = player_data.get("guild")
        race_skills = player_race.get("skills")

        race_instance, created = Race.objects.get_or_create(
            name=player_race["name"],
            description=player_race["description"]
        )

        if race_skills:
            for skill in race_skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_instance
                )

        if player_guild:
            for guild in player_guild:
                guild_instance, created = Guild.objects.get_or_create(
                    name=guild["name"],
                    description=guild["description"]
                )
        else:
            guild_instance = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data["email"],
            bio=player_data["bio"],
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
