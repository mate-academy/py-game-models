import json
import os
import django
from db.models import Race, Skill, Guild, Player


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main():
    # Чтение players.json
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    # Цикл по игрокам, где ключ словаря — это nickname
    for nickname, pdata in players_data.items():

        # --- RACE ---
        race_data = pdata.get("race", {})
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name", "Unknown"),
            defaults={"description": race_data.get("description", "")}
        )

        # --- SKILLS ---
        for skill in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill.get("name", "Unknown"),
                race=race,
                defaults={"bonus": skill.get("bonus", 0)}
            )

        # --- GUILD ---
        guild = None
        guild_data = pdata.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name", "Unknown"),
                defaults={"description": guild_data.get("description", "")}
            )

        # --- PLAYER ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata.get("email", ""),
                "bio": pdata.get("bio", ""),
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
