import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for player_name, player_info in players_data.items():
        race_obj, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"]["description"]}
        )

        for skill in player_info["race"]["skills"]:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skill["name"],
                defaults={"bonus": skill["bonus"], "race": race_obj}
            )
        if player_info["guild"] is not None:
            guild_obj, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={"description": player_info["guild"]["description"]}
            )
        else:
            guild_obj = None

        Player.objects.create(
            nickname=player_name,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
