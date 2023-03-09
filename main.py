import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players = json.load(data_file)

    for player, player_data in players.items():

        player_race = Race.objects.get_or_create(
            name=player_data.get("race")["name"],
            description=player_data.get("race")["description"]
        )[0]

        if player_data.get("race")["skills"]:
            for skill in player_data.get("race")["skills"]:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=Race.objects.get(name=player_data.get("race")["name"])
                )

        player_guild = Guild.objects.get_or_create(
            name=player_data.get("guild")["name"],
            description=player_data.get("guild")["description"]
        )[0] if player_data.get("guild") else None

        Player.objects.create(
            nickname=player,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
