import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players_info = json.load(players_file)

    for player, player_inf in players_info.items():
        race, race_done = Race.objects.get_or_create(
            name=player_inf["race"]["name"],
            description=player_inf["race"]["description"],
        )
        if race_done:
            if skills := player_inf["race"].get("skills"):
                for skill in skills:
                    Skill.objects.get_or_create(
                        name=skill.get("name"),
                        bonus=skill.get("bonus"),
                        race=race
                    )

        if guild := player_inf.get("guild"):
            guild, _ = Guild.objects.get_or_create(**guild)

        Player.objects.get_or_create(
            nickname=player,
            email=player_inf.get("email"),
            bio=player_inf.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
