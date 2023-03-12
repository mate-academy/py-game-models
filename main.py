import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for name, info in players.items():
        player_race, _ = Race.objects.get_or_create(
            name=info["race"]["name"],
            description=info["race"]["description"])
        if info["guild"] is not None:
            player_guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"])
        else:
            player_guild = None
        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player_race)
        Player.objects.create(
            nickname=name,
            email=info["email"],
            bio=info["bio"],
            race=player_race,
            guild=player_guild)


if __name__ == "__main__":
    main()
