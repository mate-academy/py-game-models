import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player_name, player_value in players.items():
        race_, _ = Race.objects.get_or_create(
            name=player_value["race"]["name"],
            description=player_value["race"]["description"]
        )

        if player_value["guild"]:
            guild_, _ = Guild.objects.get_or_create(
                name=player_value["guild"]["name"],
                description=player_value["guild"]["description"]
            )
        else:
            guild_ = None

        for skill_data in player_value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race_
            )

        Player.objects.get_or_create(
            nickname=player_name,
            email=player_value["email"],
            bio=player_value["bio"],
            race=race_,
            guild=guild_
        )


if __name__ == "__main__":
    main()
