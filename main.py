import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for nickname, data in players.items():
        email = data["email"]
        bio = data["bio"]

        race_data = data["race"]
        race_name = race_data["name"]
        race_description = race_data.get("description")

        race_obj, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description},
        )

        for skill_data in race_data.get("skills", []):
            skill_name = skill_data["name"]
            skill_bonus = skill_data["bonus"]

            Skill.objects.get_or_create(
                name=skill_name,
                race=race_obj,
                defaults={"bonus": skill_bonus},
            )

        guild_data = data.get("guild")
        guild_obj = None

        if guild_data:
            guild_name = guild_data["name"]
            guild_description = guild_data.get("description")

            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={"description": guild_description},
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": email,
                "bio": bio,
                "race": race_obj,
                "guild": guild_obj,
            },
        )


if __name__ == "__main__":
    main()
