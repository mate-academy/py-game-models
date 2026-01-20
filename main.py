import json
import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json") as f:
        data = json.load(f)

    for nickname, data in data.items():

        race_name = data["race"]["name"]
        race_desc = data["race"].get("description", "")
        race, _ = Race.objects.get_or_create(
            name=race_name,
            description=race_desc
        )

        for skill_info in data["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_info["name"],
                defaults={
                    "bonus": skill_info["bonus"],
                    "race": race
                })

        guild = None
        if data.get("guild"):
            guild_name = data["guild"]["name"]
            guild_desc = data["guild"].get("description")
            guild, _ = Guild.objects.get_or_create(
                name=guild_name,
                defaults={
                    "description": guild_desc
                }
            )

        Player.objects.get_or_create(
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
