import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def get_data_from_file() -> dict:
    with open("players.json", "r") as source_file:
        return json.load(source_file)


def main() -> None:
    players_data = get_data_from_file()
    for name, data in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=data.get("race").get("name"),
            description=data.get("race").get("description")
        )

        if skills := data.get("race").get("skills"):
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race
                )

        if guild := data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )

        Player.objects.get_or_create(
            nickname=name,
            email=data.get("email"),
            bio=data.get("bio"),
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
