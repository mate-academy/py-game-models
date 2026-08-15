import init_django_orm  # noqa: F401
import json
from django.utils import timezone
from db.models import Race, Skill, Guild, Player


def main() -> None:
    with open("players.json", "r") as file:
        raw_data = json.load(file)

    if isinstance(raw_data, dict):
        players_data = raw_data.get("players", raw_data)
    else:
        players_data = raw_data

    items = (
        players_data.items()
        if isinstance(players_data, dict)
        else enumerate(players_data)
    )

    for key, player_info in items:
        if isinstance(player_info, dict):
            fallback_name = key if isinstance(key, str) else None
            nickname = player_info.get("nickname", fallback_name)
        else:
            nickname = key if isinstance(key, str) else None
            player_info = {}

        if not nickname:
            continue

        race_data = player_info.get("race", {})
        if isinstance(race_data, dict):
            race_name = race_data.get("name")
            race_desc = race_data.get("description", "")
            skills_list = race_data.get("skills", [])
        else:
            race_name = race_data
            race_desc = ""
            skills_list = []

        if not race_name:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_desc},
        )

        guild = None
        guild_data = player_info.get("guild")
        if guild_data:
            if isinstance(guild_data, dict):
                guild_name = guild_data.get("name")
                guild_desc = guild_data.get("description")
            else:
                guild_name = guild_data
                guild_desc = None

            if guild_name:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_name,
                    defaults={"description": guild_desc},
                )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_info.get("email"),
                "bio": player_info.get("bio", ""),
                "race": race,
                "guild": guild,
                "created_at": timezone.now(),
            },
        )

        for skill_data in skills_list:
            is_dict = isinstance(skill_data, dict)
            skill_name = skill_data.get("name") if is_dict else None
            skill_bonus = skill_data.get("bonus") if is_dict else None

            if skill_name and skill_bonus:
                Skill.objects.get_or_create(
                    name=skill_name,
                    defaults={
                        "bonus": skill_bonus,
                        "race": race,
                    },
                )


if __name__ == "__main__":
    main()
