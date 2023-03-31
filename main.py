import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as source_file:
        players = json.load(source_file)

    for player_name, player_data in players.items():
        nickname = player_name
        email = player_data.get("email")
        bio = player_data.get("bio")

        race_data = player_data.get("race")
        race_name = race_data.get("name")
        race_description = race_data.get("description")

        race, created = Race.objects.get_or_create(
            name=race_name,
            description=race_description
        )

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")

            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        race_skills = race_data.get("skills")

        for skill in race_skills:
            skill_name = skill.get("name")
            skill_bonus = skill.get("bonus")
            skill_race = Race.objects.get(name=race_name)

            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=skill_race
            )

        Player.objects.create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
