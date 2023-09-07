import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player, players_data in players.items():
        nickname = player
        email = players_data["email"]
        bio = players_data["bio"]

        race_name = players_data["race"]["name"]
        race_description = players_data["race"]["description"]
        if Race.objects.filter(name=race_name).exists():
            race = Race.objects.get(name=race_name)
        else:
            race = Race.objects.create(
                name=race_name,
                description=race_description
            )

        skills = players_data["race"]["skills"]
        for skill in skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            if not Skill.objects.filter(name=skill_name).exists():
                Skill.objects.create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race
                )

        if players_data["guild"] is None:
            guild = None
        else:
            guild_name = players_data["guild"]["name"]
            guild_description = players_data["guild"]["description"]
            if Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.get(name=guild_name)
            else:
                guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )

        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(
                nickname=nickname,
                email=email,
                bio=bio,
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
