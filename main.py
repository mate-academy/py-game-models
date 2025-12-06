import json

import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as f:
        players = json.load(f)

    for nickname, player_desc_dict in players.items():
        if not isinstance(player_desc_dict, dict):
            raise ValueError(
                f"Player {nickname} has invalid structure in input data"
            )

        email = player_desc_dict.get("email")
        if not email:
            raise ValueError(
                f"Player {nickname} has no 'email' in input data"
            )

        bio = player_desc_dict.get("bio")
        if not bio:
            raise ValueError(
                f"Player {nickname} has no 'bio' in input data"
            )

        race_data = player_desc_dict.get("race")
        if not race_data or not isinstance(race_data, dict):
            raise ValueError(
                f"Player {nickname} has no valid 'race' in input data"
            )

        race_name = race_data.get("name")
        if not race_name:
            raise ValueError(
                f"Player {nickname}: race has no 'name'"
            )

        race_desc = race_data.get("description")

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={
                "description": race_desc,
            },
        )

        skills = race_data.get("skills")
        if skills:
            for skill in skills:
                if not isinstance(skill, dict):
                    raise ValueError(
                        f"Player {nickname}: skill has invalid structure"
                    )

                skill_name = skill.get("name")
                skill_bonus = skill.get("bonus")
                if not skill_name or not skill_bonus:
                    raise ValueError(
                        f"Player {nickname}: skill is missing "
                        "'name' or 'bonus'"
                    )

                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "bonus": skill_bonus,
                        "race": race_obj,
                    },
                )

        guild_obj = None
        guild_data = player_desc_dict.get("guild")
        if guild_data:
            if not isinstance(guild_data, dict):
                raise ValueError(
                    f"Player {nickname}: guild has invalid structure"
                )

            guild_name = guild_data.get("name")
            if not guild_name:
                raise ValueError(
                    f"Player {nickname}: guild has no 'name'"
                )

            guild_description = guild_data.get("description")
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": guild_description,
                },
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_obj,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
