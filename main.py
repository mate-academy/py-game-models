import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_dict = json.load(file)

    for nickname, data in players_dict.items():
        race_data = data["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")},
        )

        for skill_item in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_item["name"],
                defaults={
                    "bonus": skill_item["bonus"],
                    "race": race_obj,
                },
            )

        guild_obj = None
        guild_data = data.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race_obj,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
