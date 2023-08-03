import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)
    for player in data:
        if not Race.objects.filter(name=data[player]["race"]["name"]).exists():
            Race.objects.create(
                name=data[player]["race"]["name"],
                description=data[player]["race"]["description"]
            )
        player_race = Race.objects.get(name=data[player]["race"]["name"])
        for skill in data[player]["race"]["skills"]:
            if not Skill.objects.filter(name=skill["name"]).exists():
                Skill.objects.create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=player_race
                )
        if data[player]["guild"] is not None:
            if not Guild.objects.filter(
                    name=data[player]["guild"]["name"]
            ).exists():
                Guild.objects.create(
                    name=data[player]["guild"]["name"],
                    description=data[player]["guild"]["description"]
                )
            player_guild = Guild.objects.get(
                name=data[player]["guild"]["name"]
            )
        else:
            player_guild = None
        if not Player.objects.filter(nickname=player).exists():
            Player.objects.create(
                nickname=player,
                email=data[player]["email"],
                bio=data[player]["bio"],
                race=player_race,
                guild=player_guild
            )


if __name__ == "__main__":
    main()
