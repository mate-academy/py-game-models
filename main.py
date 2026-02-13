import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)

    for nickname, player_data in data.items():

        race_data = player_data.get("race")
        if not race_data:
            continue

        race_name = race_data.get("name")
        race_description = race_data.get("description")

        if not race_name:
            continue

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_description or "",
        )

        for skill in race_data.get("skills", []):
            skill_name = skill.get("name")
            skill_bonus = skill.get("bonus")

            if not skill_name or not skill_bonus:
                continue

            Skill.objects.get_or_create(
                name=skill_name,
                bonus=skill_bonus,
                race=race_obj,
            )

        guild_obj = None
        guild_data = player_data.get("guild")

        if guild_data:
            guild_name = guild_data.get("name")
            if guild_name:
                guild_obj, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    description=guild_data.get("description"),
                )

        email = player_data.get("email")
        bio = player_data.get("bio")

        if not email or not bio:
            continue

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race_obj,
            guild=guild_obj,
        )


if __name__ == "__main__":
    main()
