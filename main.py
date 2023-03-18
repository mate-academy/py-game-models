import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    races = {}
    skills = {}
    guilds = {}

    for player_name, player_data in data.items():
        race_name = player_data.get("race").get("name")
        guild_name = player_data.get("guild").get("name") if player_data.get(
            "guild"
        ) else None

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "description": player_data.get("race").get("description")
            }
        )
        races[race_name] = race

        if guild_name:
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": player_data.get("guild").get(
                        "description"
                    )
                }
            )
            guilds[guild_name] = guild

        for skill_data in player_data.get("race").get("skills"):
            skill_name = skill_data.get("name")
            if skill_name not in skills:
                skill = Skill.objects.create(
                    name=skill_name, bonus=skill_data.get("bonus"), race=race
                )
                skills[skill_name] = skill

        Player.objects.create(
            nickname=player_name, email=player_data.get("email"),
            bio=player_data.get("bio"), race=race,
            guild=guilds.get(guild_name))


if __name__ == "__main__":
    main()
