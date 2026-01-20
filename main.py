import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for player in data:
        race = data[player]["race"]
        this_player_race_obj, created_race = Race.objects.get_or_create(
            name=race["name"],
            description=race["description"])

        for skill in race["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=this_player_race_obj)

        guild = data[player]["guild"]
        if guild is not None:
            this_player_guild_obj, created_guild = Guild.objects.get_or_create(
                name=guild["name"],
                description=guild["description"])
        if guild is None:
            this_player_guild_obj = None

        Player.objects.create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=this_player_race_obj,
            guild=this_player_guild_obj)


if __name__ == "__main__":
    main()
