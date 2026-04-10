import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild
from django.db import transaction


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for nickname, item in data.items():
        if not isinstance(item, dict):
            continue

        with transaction.atomic():
            email = item.get("email", "")
            bio = item.get("bio") or ""

            race_info = item.get("race")
            if isinstance(race_info, dict):
                race_name = race_info.get("name")
                race_description = race_info.get("description")
            else:
                race_name = race_info
                race_description = None

            if not race_name:
                continue

            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_description}
            )
            skills_list = []
            for sk in race_info.get("skills", []):
                skill_name = sk.get("name")
                if not skill_name:
                    continue
                bonus = sk.get("bonus", "")
                skill, _ = Skill.objects.get_or_create(
                    name=skill_name,
                    race=race,
                    defaults={"bonus": bonus}
                )
                skills_list.append(skill)

            guild = None
            guild_info = item.get("guild")
            if guild_info:
                if isinstance(guild_info, dict):
                    guild_name = guild_info.get("name")
                    guild_description = guild_info.get("description")
                else:
                    guild_name = guild_info
                    guild_description = None
                if guild_name:
                    guild, _ = Guild.objects.get_or_create(
                        name=guild_name,
                        defaults={"description": guild_description}
                    )

            player, _ = Player.objects.get_or_create(
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
