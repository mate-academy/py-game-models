import init_django_orm  # noqa: F401

import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)
    # 1. Race
    for nickname, data in players_data.items():
        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

    # 2. Skill
        for skil in race_data["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skil["name"],
                defaults={
                    "bonus": skil.get("bonus", ""),
                    "race": race
                }
            )

    # 3. Guild
        guild = None
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

    # 4. Player
        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
