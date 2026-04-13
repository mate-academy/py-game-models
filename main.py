import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild
from django.db import transaction


def main() -> None:
    with open("players.json", "r") as players_file:
        players_dict = json.load(players_file)

    for nickname, info in players_dict.items():
        with transaction.atomic():
            race_info = info.get("race")
            if isinstance(race_info, dict):
                race_name = race_info.get("name")
                race_desc = race_info.get("description")
            else:
                race_name = race_info
                race_desc = None

            if not race_name:
                continue

            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_desc}
            )

            skills_iter = []
            if isinstance(race_info, dict):
                skills_iter.extend(race_info.get("skills") or [])
            skills_iter.extend(info.get("skills") or [])
            for skills_info in skills_iter:
                sk_name = skills_info.get("name")
                if not sk_name:
                    continue
                bonus = skills_info.get("bonus", "")
                Skill.objects.get_or_create(
                    name=sk_name,
                    race=race,
                    defaults={"bonus": bonus}
                )

            guild = None
            guild_info = info.get("guild")
            if guild_info:
                if not isinstance(guild_info, dict):
                    guild_info = {"name": guild_info, "description": None}

                g_name = guild_info.get("name")
                g_desc = guild_info.get("description")
                if g_name:
                    guild, _ = Guild.objects.get_or_create(
                        name=g_name,
                        defaults={"description": g_desc}
                    )

            Player.objects.get_or_create(
                nickname=nickname,
                defaults={
                    "email": info.get("email", ""),
                    "bio": info.get("bio", ""),
                    "race": race,
                    "guild": guild,
                }
            )


if __name__ == "__main__":
    main()
