import json
from pathlib import Path
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild

def main() -> None:
    players_file = Path("players.json")

    if not players_file.exists():
        print("\u274c Файл players.json не знайдено!")
        return

    with open(players_file, "r", encoding="utf-8") as file:
        try:
            players_data = json.load(file)
            if not isinstance(players_data, dict):
                print("\u274c Некоректний формат JSON: очікується словник!")
                return
        except json.JSONDecodeError:
            print("\u274c Помилка декодування JSON!")
            return

    print("\u2705 Дані зчитано, починаємо обробку...\n")

    for nickname, player in players_data.items():
        if not isinstance(player, dict):
            print(f"⚠️ Некоректний формат гравця: {player}")
            continue

        race_data = player.get("race", {})
        race, created = Race.objects.get_or_create(
            name=race_data.get("name", "Unknown"),
            defaults={"description": race_data.get("description", "")}
        )
        if created:
            print(f"✅ Додано расу: {race.name}")

        for skill_data in race_data.get("skills", []):
            if isinstance(skill_data, dict):
                skill, skill_created = Skill.objects.get_or_create(
                    name=skill_data.get("name", "Unknown"),
                    race=race,
                    defaults={"bonus": skill_data.get("bonus", "")}
                )
                if skill_created:
                    print(f"✅ Додано навик: {skill.name} для раси {race.name}")

        guild = None
        guild_data = player.get("guild")
        if isinstance(guild_data, dict):
            guild, guild_created = Guild.objects.get_or_create(
                name=guild_data.get("name", "Unknown"),
                defaults={"description": guild_data.get("description", "")}
            )
            if guild_created:
                print(f"✅ Додано гільдію: {guild.name}")

        player_obj, player_created = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )
        if player_created:
            print(f"✅ Додано гравця: {player_obj.nickname}")

if __name__ == "__main__":
    main()
