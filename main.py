import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player, value in data.items():
        player_race, created = Race.objects.get_or_create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )
        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race
            )
        if value["guild"] is not None:
            player_guild, created = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                description=value["guild"]["description"]
            )
        else:
            player_guild = None
        Player.objects.get_or_create(
            nickname=player,
            email=value["email"],
            bio=value["bio"],
            race=player_race,
            guild=player_guild
        )


if __name__ == "__main__":
    main()
