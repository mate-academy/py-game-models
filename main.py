import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        player_storages = json.load(data_file)
    for player in player_storages:
        race_info = player_storages.get(player).get("race")
        race_name = race_info.get("name")
        race_description = race_info.get("description")
        race, created = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )
        skill_storages = race_info.get("skills", [])
        [Skill.objects.get_or_create(
            name=skill.get("name"),
            bonus=skill.get("bonus"),
            race=race
        )
            for skill in skill_storages]
        guilds_info = player_storages.get(player).get("guild")
        if guilds_info:
            guilds_name = guilds_info.get("name")
            guilds_description = guilds_info.get("description")
            guilds, created = Guild.objects.get_or_create(
                name=guilds_name,
                description=guilds_description
            )
        else:
            guilds = None
        human_email = player_storages.get(player).get("email")
        human_bio = player_storages.get(player).get("bio")
        Player.objects.create(
            nickname=player,
            email=human_email,
            bio=human_bio,
            race=race,
            guild=guilds
        )


if __name__ == "__main__":
    main()
