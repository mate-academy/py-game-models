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

        if not Race.objects.filter(name=race_name).exists():
            race = Race.objects.create(
                name=race_name,
                description=race_description
            )
        else:
            race = Race.objects.get(name=race_name)

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")

            if not Guild.objects.filter(name=guild_name).exists():
                guild = Guild.objects.create(
                    name=guild_name,
                    description=guild_description
                )
            else:
                guild = Guild.objects.get(name=guild_name)

        race_skills = race_data.get("skills")

        for skill in race_skills:
            skill_name = skill.get("name")
            skill_bonus = skill.get("bonus")

            if not Skill.objects.filter(name=skill_name).exists():
                skill_race = Race.objects.get(name=race_name)

                Skill.objects.create(
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
