import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("./players.json", "rb") as players_data_json:
        players_data = json.load(players_data_json)

        for player_name, player_data in players_data.items():
            print(player_data, "player_data")
            player_data_race = player_data.get("race", dict())
            player_race = Race.objects.get_or_create(
                name=player_data_race.get("name"),
                description=player_data_race.get("description"),
            )

            for skill_data in player_data_race.get("skills"):
                Skill.objects.get_or_create(
                    race=player_race[0],
                    **skill_data
                )

            Player.objects.get_or_create(
                nickname=player_name,
                email=player_data.get("email"),
                bio=player_data.get("bio"),
                race=player_race[0],
                guild=(
                    Guild.objects.get_or_create(
                        **player_data.get("guild")
                    )[0] if player_data.get("guild") else None
                )
            )


if __name__ == "__main__":
    main()
