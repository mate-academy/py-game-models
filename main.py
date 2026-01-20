import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)

    for name in players.keys():
        race = players.get(name, {}).get("race", {})
        race_name = race.get("name")
        race_description = race.get("description")

        race_object, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        guild_object = None

        skills = race.get("skills", [])
        if skills:
            for skill in skills:
                skill_name = skill["name"]
                skill_bonus = skill["bonus"]
                Skill.objects.get_or_create(
                    name=skill_name,
                    bonus=skill_bonus,
                    race=race_object
                )

        guild = players.get(name, {}).get("guild")
        if guild is not None:
            guild_name = guild.get("name")
            guild_description = guild.get("description")
            guild_object, _ = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        Player.objects.create(
            nickname=name,
            email=players.get(name, {}).get("email"),
            bio=players.get(name, {}).get("bio"),
            race=race_object,
            guild=guild_object
        )


if __name__ == "__main__":
    main()
