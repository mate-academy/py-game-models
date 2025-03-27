import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as players_file:
        players = json.load(players_file)

    for username, user_data in players.items():
        race, race_created = Race.objects.get_or_create(
            name=user_data.get("race").get("name"),
            description=user_data.get("race").get("description"),
        )
        if race_created:
            for skill in user_data.get("race").get("skills"):
                Skill.objects.get_or_create(
                    name=skill.get("name"),
                    bonus=skill.get("bonus"),
                    race=race,
                )

        guild = None

        if user_data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=user_data.get("guild").get("name"),
                description=user_data.get("guild").get("description"),
            )

        Player.objects.get_or_create(
            nickname=username,
            email=user_data.get("email"),
            bio=user_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
