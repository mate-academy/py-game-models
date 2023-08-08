import json

from django.db.utils import IntegrityError

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player in data:
        race_details = data[player]["race"]
        skill_details = race_details["skills"]
        current_guild = data[player]["guild"]

        if not Race.objects.filter(name=race_details["name"]).exists():
            Race.objects.create(
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

        try:
            Player.objects.create(
                nickname=str(player).capitalize(),  # capitalize()?
                email=data[player]["email"],
                bio=data[player]["bio"],
                race_id=current_race,
                guild_id=current_guild,
            )
        except IntegrityError as e:
            print(f"Name already taken: {e}")


if __name__ == "__main__":
    main()
