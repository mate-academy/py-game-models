import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player_name in data:
        player = data[player_name]

        # Create player
        player_data = {
            "nickname": player_name,
            "email": player.get("email"),
            "bio": player.get("bio"),
            "race": Race.objects.get_or_create(
                name=player["race"]["name"],
                description=player["race"]["description"]
            )[0],
            "guild": (
                None if not player["guild"]
                else Guild.objects.get_or_create(
                    name=player["guild"]["name"],
                    description=player["guild"]["description"]
                )[0]
            )
        }
        Player.objects.create(**player_data)

        # Define race-related skills
        race = player_data["race"]
        for skill in player["race"]["skills"]:
            race.skill_set.get_or_create(
                name=skill.get("name"),
                bonus=skill.get("bonus"),
                race=race
            )


if __name__ == "__main__":
    main()
