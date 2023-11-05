import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for nickname, player_data in players.items():
        email, bio, race, guild = player_data.values()

        race_instance, created = Race.objects.get_or_create(
            name=race.get("name"),
            description=race.get("description")
        )

        skills = race.get("skills")
        if skills:
            for skill in skills:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race_instance
                )

        if guild:
            guild_instance, created = Guild.objects.get_or_create(
                name=guild.get("name"),
                description=guild.get("description")
            )
        else:
            guild_instance = None

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_instance,
            guild=guild_instance
        )


if __name__ == "__main__":
    main()
