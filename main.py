import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        player_storages = json.load(data_file)

    for player_name, player_data in player_storages.items():
        race, created = Race.objects.get_or_create(
            name=player_data.get("race").get("name"),
            description=player_data.get("race").get("description"),
        )

        skill_storages = player_data.get("race").get("skills", [])
        [
            Skill.objects.get_or_create(
                name=skill.get("name"), bonus=skill.get("bonus"), race=race
            )
            for skill in skill_storages
        ]

        if player_data.get("guild"):
            guilds, created = Guild.objects.get_or_create(
                name=player_data.get("guild").get("name"),
                description=player_data.get("guild").get("description"),
            )
        else:
            guilds = None

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guilds,
        )


if __name__ == "__main__":
    main()
