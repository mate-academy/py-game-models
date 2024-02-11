import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_json:
        players_data = json.load(players_json)

    print(players_data)
    for players_nickname, players_info in players_data.items():

        race, _ = Race.objects.get_or_create(
            name=players_info["race"]["name"],
            description=players_info["race"]["description"]
        )

        guild_info = players_info["guild"]
        guild = None
        if guild_info:
            guild, _ = Guild.objects.get_or_create(
                name=players_info["guild"]["name"],
                description=players_info["guild"]["description"]
            )

        Player.objects.create(
            nickname=players_nickname,
            email=players_info["email"],
            bio=players_info["bio"],
            race=race,
            guild=guild
        )

        for skill_info in players_info["race"]["skills"]:
            skill_name = skill_info["name"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_info["bonus"],
                    race=race
                )


if __name__ == "__main__":
    main()
