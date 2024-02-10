import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as players:
        players = json.load(players)

    for player, player_data in players.items():
        race_info = {
            "name": player_data["race"]["name"],
            "description": player_data["race"]["description"]
        }
        race, _ = Race.objects.get_or_create(**race_info)

        guild_info = player_data["guild"]
        if guild_info:
            guild, _ = Guild.objects.get_or_create(**guild_info)
        else:
            guild = None

        skills_info = player_data["race"]["skills"]
        for skill_data in skills_info:
            skill_data["race"] = race
            skill, _ = Skill.objects.get_or_create(**skill_data)

        player_info = {
            "nickname": player,
            "email": player_data["email"],
            "bio": player_data["bio"],
            "race": race,
            "guild": guild
        }

        Player.objects.create(**player_info)


if __name__ == "__main__":
    main()
