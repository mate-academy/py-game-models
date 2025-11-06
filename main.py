import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as json_file:
        players = json.load(json_file)

    for nickname, pdata in players.items():
        email = pdata.get("email")
        bio = pdata.get("bio")

        race_info = pdata.get("race")
        if race_info:
            race_name = race_info.get("name")
            race_desc = race_info.get("description")
            skills = race_info.get("skills", [])

            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_desc},
            )

            for skill_info in skills:
                skill_name = skill_info.get("name")
                skill_bonus = skill_info.get("bonus")

                if skill_name:
                    Skill.objects.get_or_create(
                        name=skill_name,
                        defaults={
                            "bonus": skill_bonus,
                            "race": race,
                        },
                    )

        guild = None
        guild_info = pdata.get("guild")
        if guild_info:
            guild_name = guild_info.get("name")
            guild_description = guild_info.get("description")

            guild, guild_created = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        player, player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
