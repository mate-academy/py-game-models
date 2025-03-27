import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as data_file:
        players = json.load(data_file)

    for player_name, player_data in players.items():
        race, created = Race.objects.get_or_create(
            name=player_data.get("race").get("name"),
            description=player_data.get("race").get("description"),
        )

        skills = player_data.get("race").get("skills", [])
        [
            Skill.objects.get_or_create(
                name=skill.get("name"), bonus=skill.get("bonus"), race=race
            )
            for skill in skills
        ]

        if player_data.get("guild"):
            guild, created = Guild.objects.get_or_create(
                name=player_data.get("guild").get("name"),
                description=player_data.get("guild").get("description"),
            )
        else:
            guild = None

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
