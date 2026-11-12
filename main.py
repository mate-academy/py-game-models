import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as players_file:
        players_data = json.load(players_file)

    for player in players_data:
        race_dict = players_data.get(player)["race"]
        race, _ = Race.objects.get_or_create(
            name=race_dict["name"], description=race_dict["description"]
        )

        skills_list = players_data.get(player)["race"]["skills"]
        if skills_list:
            for current_skill in skills_list:
                skill, _ = Skill.objects.get_or_create(
                    name=current_skill["name"],
                    bonus=current_skill["bonus"],
                    race=race
                )

        guild_dict = players_data.get(player)["guild"]
        if guild_dict:
            guild, _ = Guild.objects.get_or_create(
                name=guild_dict["name"],
                description=guild_dict["description"]
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player,
            email=players_data.get(player)["email"],
            bio=players_data.get(player)["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
