import os
import django
import json
from db.models import Race, Skill, Player, Guild

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for nickname, player_data in data.items():
        race_data = player_data.get("race", {})
        race_name = race_data.get("name")
        race_description = race_data.get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        skills_list = race_data.get("skills", [])
        for skill_data in skills_list:
            skill_name = skill_data.get("name")
            skill_bonus = skill_data.get("bonus")
            Skill.objects.get_or_create(
                name=skill_name,
                race=race,
                defaults={"bonus": skill_bonus}
            )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data.get("email", ""),
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
