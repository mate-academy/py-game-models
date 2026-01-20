import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players_data = json.load(data_file)

    for player, player_info in players_data.items():
        race_info = player_info.get("race")
        skill_info = race_info.get("skills")
        guild_info = player_info.get("guild")

        new_race, created = Race.objects.get_or_create(
            name=race_info["name"],
            description=race_info["description"]
        )

        for skill in skill_info:
            new_skill, created = Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=new_race
            )

        if guild_info:
            new_guild, created = Guild.objects.get_or_create(
                name=guild_info["name"],
                description=guild_info["description"]
            )
        else:
            new_guild = None

        Player.objects.create(
            nickname=player,
            email=player_info["email"],
            bio=player_info["bio"],
            race=new_race,
            guild=new_guild,
        )


if __name__ == "__main__":
    main()
