import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_details in data.items():
        current_guild = player_details[1]["guild"]
        race_details = player_details[1]["race"]
        skill_details = race_details["skills"]

        # Race.objects.get_or_create(
        #     name=race_details["name"],
        #     description=race_details["description"]
        # )
        # current_race = Race.objects.get(name=race_details["name"]).id

        if not Race.objects.filter(name=race_details["name"]).exists():
            Race.objects.get_or_create(
                name=race_details["name"],
                description=race_details["description"]
            )
            current_race = Race.objects.get(name=race_details["name"]).id

        for skill in skill_details:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race_id=current_race
                )

        if current_guild is not None:
            if not Guild.objects.filter(name=current_guild["name"]).exists():
                Guild.objects.create(
                    name=current_guild["name"],
                    description=current_guild["description"]
                )
            current_guild = Guild.objects.get(name=current_guild["name"]).id

        Player.objects.get_or_create(
            nickname=str(player_details[0]),
            email=player_details[1]["email"],
            bio=player_details[1]["bio"],
            race_id=current_race,
            guild_id=current_guild,
        )


if __name__ == "__main__":
    main()
