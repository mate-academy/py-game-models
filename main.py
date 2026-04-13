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
            if not isinstance(race_info, dict):
                race_info = {"name": race_info, "description": None}

            race_name = race_info.get("name")
            if not race_name:
                continue

            race, _ = Race.objects.get_or_create(
                name=race_name,
                defaults={"description": race_info.get("description")}
            )

            skills_data = info.get("skills") or []
            if isinstance(info.get("race"), dict):
                skills_data += info["race"].get("skills") or []

            for sk_info in skills_data:
                sk_name = sk_info.get("name")
                if sk_name:
                    Skill.objects.get_or_create(
                        name=sk_name,
                        defaults={
                            "bonus": sk_info.get("bonus", ""),
                            "race": race
                        }
                    )

            guild = None
            guild_info = info.get("guild")
            if guild_info:
                if not isinstance(guild_info, dict):
                    guild_info = {"name": guild_info, "description": None}

                g_name = guild_info.get("name")
                if g_name:
                    guild, _ = Guild.objects.get_or_create(
                        name=g_name,
                        defaults={"description": guild_info.get("description")}
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
