import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player in data:
        player_race, created = Race.objects.get_or_create(
            name=data[player]["race"]["name"],
            description=data[player]["race"]["description"]
        )
        for skill in data[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )
        if data[player]["guild"] is not None:
            player_guild, created = Guild.objects.get_or_create(
                name=data[player]["guild"]["name"],
                description=data[player]["guild"]["description"]
            )
        else:
            player_guild = None
        Player.objects.get_or_create(
            nickname=player,
            email=data[player]["email"],
            bio=data[player]["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
