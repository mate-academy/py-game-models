import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        race_data = data["race"]
        race_obj, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skills_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skills_data["name"],
                defaults={
                    "bonus": skills_data["bonus"],
                    "race": race_obj
                }
            )

        guild_obj = None
        guild_data = data.get("guild")
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data["bio"],
                "race": race_obj,
                "guild": guild_obj,
            }
        )


if __name__ == "__main__":
    main()
