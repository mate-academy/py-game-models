import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        json_data = json.load(f)
    for player in json_data:
        guild = json_data[player]["guild"]
        if guild is not None:
            player_guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"]
            )
        else:
            player_guild = [None]
        race = json_data[player]["race"]
        player_race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"]
        )
        skills = race["skills"]
        for skill in skills:
            if skill["name"] not in Skill.objects.all().values_list("name"):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race[0]
                )
        Player.objects.get_or_create(
            nickname=player,
            email=json_data[player]["email"],
            bio=json_data[player]["bio"],
            race=player_race[0],
            guild=player_guild[0]
        )


if __name__ == "__main__":
    main()
