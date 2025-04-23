import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild

from django.utils import timezone


def main() -> None:
    with open("players.json", "r") as f:
        players = json.load(f)

    for nickname, data in players.items():
        # Получаем или создаём расу
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            defaults={"description": data["race"].get("description", "")}
        )

        # Добавляем все скиллы расы
        for skill_data in data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        # Обрабатываем гильдию (она может быть None)
        guild = None
        if data.get("guild"):
            guild, _ = Guild.objects.get_or_create(
                name=data["guild"]["name"],
                defaults={"description": data["guild"]["description"]}
            )

        # Создаём игрока
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild,
            }
        )

if __name__ == "__main__":
    main()
