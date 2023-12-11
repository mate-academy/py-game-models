import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player_name, player_data in data.items():
        race_data = player_data.get("race")
        guild_data = player_data.get("guild")
        skills_data = race_data.get("skills")

        race, created = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description")
        )

        guild = None
        if guild_data:
            guild, created = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description")
            )

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data.get("name"),
                bonus=skill_data.get("bonus"),
                race=race
            )

        Player.objects.create(
            nickname=player_name,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild
        )





if __name__ == "__main__":
    main()
