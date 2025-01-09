import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        players_data = json.load(file)

    # Шаг 2: Итерация по данным и добавление в базу данных
    for nickname, player_data in players_data.items():
        # Шаг 2.1: Создать или получить Race
        race_data = player_data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )

        # Шаг 2.2: Создать или получить Skills для Race
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={"bonus": skill_data["bonus"], "race": race}
            )

        # Шаг 2.3: Создать или получить Guild (если указана)
        guild = None
        if player_data.get("guild"):
            guild_data = player_data["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # Шаг 2.4: Создать Player
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            }
        )


if __name__ == "__main__":
    main()
