import os
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "players.json")

    with open(json_path) as file:
        data = json.load(file)

    for nickname, item in data.items():
        race_raw = item["race"]
        race, _ = Race.objects.get_or_create(
            name=race_raw["name"],
            defaults={"description": race_raw["description"]}
        )

        for skill_raw in race_raw.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_raw["name"],
                defaults={
                    "bonus": skill_raw["bonus"],
                    "race": race,
                }
            )

        guild = None
        if item.get("guild"):
            guild_raw = item["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_raw["name"],
                defaults={"description": guild_raw["description"]}
            )

        Player.objects.create(
            nickname=nickname,
            email=item["email"],
            bio=item["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
