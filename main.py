import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source_file:
        players_data = json.load(source_file)

    for name, player_info in players_data.items():
        guild_ = None
        player_guild = player_info["guild"]

        if player_guild:
            guild_, _ = Guild.objects.get_or_create(
                name=player_guild["name"],
                defaults={"description": player_guild["description"]},
            )

        race_ = None
        player_race = player_info["race"]

        if player_race:
            race_, created = Race.objects.get_or_create(
                name=(player_race["name"]),
                defaults={"description": player_race["description"]},
            )

            if created:
                skills = player_race["skills"]

                for skill in skills:
                    Skill.objects.create(
                        name=skill["name"],
                        bonus=skill["bonus"],
                        race=race_,
                    )

        Player.objects.create(
            nickname=name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_,
            guild=guild_,
        )


if __name__ == "__main__":
    main()
