import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_dict = json.load(players_file)
    for user, user_info in players_dict.items():
        race, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            description=user_info["race"]["description"]
        )
        for skill in user_info["race"].get("skills",
                                           []):
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race
            )
        guild = None
        if user_info.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=user_info["guild"]["name"],
                description=user_info["guild"]["description"]
            )
        Player.objects.get_or_create(
            nickname=user,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
