import json
import os
import django
from db.models import Race, Guild, Skill, Player

# Konfiguracja Django, jeśli uruchamiasz plik niezależnie
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def main() -> None:
    """Wczytuje dane z players.json i dodaje je do bazy danych."""
    with open("players.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for nickname, player_data in data.items():
        race_data = player_data.get("race")
        race_name = race_data.get("name")
        race_description = race_data.get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name, defaults={"description": race_description}
        )

        guild_data = player_data.get("guild")
        guild = None
        if guild_data:
            guild_name = guild_data.get("name")
            guild_description = guild_data.get("description", None)
            guild, _ = Guild.objects.get_or_create(
                name=guild_name, defaults={"description": guild_description}
            )

        skill_objects = []
        for skill_info in race_data.get("skills", []):
            skill_name = skill_info.get("name")
            skill_bonus = skill_info.get("bonus", "")
            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                defaults={"bonus": skill_bonus, "race": race},
            )
            skill_objects.append(skill)

        player, created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data.get("bio", ""),
                "race": race,
                "guild": guild,
            },
        )
        if created:
            player.skills.set(skill_objects)


if __name__ == "__main__":
    main()
