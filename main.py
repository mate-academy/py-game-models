import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_json:
        players_data = json.load(players_json)

    print(players_data)
    for players_nickname, players_info in players_data.items():

        race, race_created = Race.objects.get_or_create(
            name=players_info["race"]["name"],
            description=players_info["race"]["description"]
        )

        if guild := players_info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=players_info["guild"]["name"],
                description=players_info["guild"]["description"]
            )

        if race_created:
            for skill_info in players_info["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_info["name"],
                    bonus=skill_info["bonus"],
                    race=race
                )

        Player.objects.create(
            nickname=players_nickname,
            email=players_info["email"],
            bio=players_info["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
