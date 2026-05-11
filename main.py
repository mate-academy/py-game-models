import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players_info = json.load(file)

    for nickname, user_info in players_info.items():
        race_obj, _ = Race.objects.get_or_create(
            name=user_info["race"]["name"],
            defaults={"description": user_info["race"]["description"]}
        )
        for skill_data in user_info["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race_obj
                }
            )
        guild_obj = None
        if user_info.get("guild"):
            guild_obj, _ = Guild.objects.get_or_create(
                name=user_info["guild"]["name"],
                defaults={"description": user_info["guild"]["description"]}
            )
        Player.objects.create(
            nickname=nickname,
            email=user_info["email"],
            bio=user_info["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
