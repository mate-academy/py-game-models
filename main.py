import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for nickname, player_dict in players.items():
        guild = None
        race, created = Race.objects.get_or_create(
            name=player_dict["race"]["name"],
            description=player_dict["race"]["description"]
        )
        for skill_dict in player_dict["race"]["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_dict["name"],
                bonus=skill_dict["bonus"],
                race=race
            )
        if player_dict["guild"] is not None:
            guild, created = Guild.objects.get_or_create(
                name=player_dict["guild"]["name"],
                description=player_dict["guild"]["description"]
            )
            guild = guild
        player, created = Player.objects.get_or_create(
            nickname=nickname,
            email=player_dict["email"],
            bio=player_dict["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
