import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players_dicts: dict[dict] = json.load(file)

    for player_name, player_dict in players_dicts.items():
        race, _ = Race.objects.get_or_create(
            name=player_dict["race"]["name"],
            description=player_dict["race"]["description"]
        )
        for skill in player_dict["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        Player.objects.create(
            nickname=player_name,
            email=player_dict["email"],
            bio=player_dict["bio"],
            race=race,
            guild=(
                Guild.objects.get_or_create(
                    name=player_dict["guild"]["name"],
                    description=player_dict["guild"]["description"],
                )[0]
                if player_dict["guild"]
                else None
            )
        )


if __name__ == "__main__":
    # main()
    print(Race.objects.get(name="elf").players.all())
