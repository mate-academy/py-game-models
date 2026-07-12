import json

import init_django_orm  # noqa: F401

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")

        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            description=race_data.get("description"),
        )

        guild = None
        guild_data = player_data.get("guild")

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                description=guild_data.get("description"),
            )

        skills = race_data.get("skills")

        for skill_data in skills:
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                bonus=skill_data.get("bonus"),
                race=race,
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=player_data.get("email"),
            bio=player_data.get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
