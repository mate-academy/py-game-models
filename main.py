import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data_players = json.load(file)

    for nickname, data_player in data_players.items():
        email = data_player["email"]
        bio = data_player["bio"]

        race_name = data_player["race"]["name"]
        race_desc = data_player["race"]["description"]
        race = Race.objects.get_or_create(
            name=race_name,
            description=race_desc,
        )[0]

        skills = data_player["race"]["skills"]
        for skill in skills:
            skill_name = skill["name"]
            skill_bonus = skill["bonus"]
            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race,
            )

        if data_player["guild"]:
            guild_name = data_player["guild"]["name"]
            guild_desc = data_player["guild"]["description"]
            guild = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_desc,
            )[0]
        else:
            guild = None

        player = Player(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild,
        )
        player.save()


if __name__ == "__main__":
    main()
