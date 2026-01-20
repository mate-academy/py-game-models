import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data_players = json.load(file)

    for nickname, data_player in data_players.items():

        race, race_created = Race.objects.get_or_create(
            name=data_player["race"]["name"],
            description=data_player["race"]["description"],
        )

        skills = data_player["race"]["skills"]
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        if data_player["guild"]:
            guild, guild_created = Guild.objects.get_or_create(
                name=data_player["guild"]["name"],
                description=data_player["guild"]["description"],
            )
        else:
            guild = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=data_player["email"],
            bio=data_player["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
