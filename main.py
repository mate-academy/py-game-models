import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for player, player_data in players.items():

        player_race, created = Race.objects.get_or_create(
            name=player_data["race"]["name"],
            description=player_data["race"]["description"])

        if created:
            if race_skills := player_data["race"]["skills"]:
                for skill in race_skills:
                    Skill.objects.get_or_create(
                        **skill,
                        race=player_race
                    )
        if guilds := player_data["guild"]:
            guilds, _ = Guild.objects.get_or_create(
                **guilds
            )

        Player.objects.get_or_create(
            nickname=player,
            email=player_data["email"],
            bio=player_data["bio"],
            race=player_race,
            guild=guilds,
        )


if __name__ == "__main__":
    main()
