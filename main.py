import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for player, player_inf in players.items():
        race, _ = Race.objects.get_or_create(
            name=player_inf["race"]["name"],
            description=player_inf["race"]["description"])

        guild = None
        if player_inf["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=player_inf["guild"]["name"],
                description=player_inf["guild"]["description"])

        Player.objects.create(nickname=player,
                              email=player_inf["email"],
                              bio=player_inf["bio"],
                              race=race,
                              guild=guild)
        for skill in player_inf["race"]["skills"]:
            Skill.objects.get_or_create(name=skill["name"],
                                        bonus=skill["bonus"],
                                        race=race)


if __name__ == "__main__":
    main()
