import init_django_orm  # noqa: F401
import json
import os

from db.models import Race, Skill, Guild, Player


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "db", "tests", "players.json")


def main() -> None:
    with open(FILE_PATH) as file:
        data = json.load(file)

    for nickname, entry in data.items():
        race_data = entry.get("race")
        if not race_data:
            continue

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description") or ""}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

        guild_data = entry.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": entry["email"],
                "bio": entry["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
