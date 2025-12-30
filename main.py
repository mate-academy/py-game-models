import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
    for nickname, player_dict in players.items():
        guild = None
        race_data = player_dict["race"]
        race, created = Race.objects.get_or_create(
            name=race_data["name"],
            description=race_data["description"]
        )
        for skill_dict in race_data["skills"]:
            skill, created = Skill.objects.get_or_create(
                name=skill_dict["name"],
                bonus=skill_dict["bonus"],
                race=race
            )
        if player_dict["guild"]:
            player_guild = player_dict["guild"]
            guild, created = Guild.objects.get_or_create(
                name=player_guild["name"],
                description=player_guild["description"]
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
