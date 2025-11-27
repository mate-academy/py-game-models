import os
import json
from db.models import Race, Skill, Guild, Player


def main() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "players.json")

    with open(json_path) as file:
        data = json.load(file)

    for nickname, item in data.items():
        race_raw = item.get("race", {})
        race_name = race_raw.get("name")
        race_description = race_raw.get("description", "")

        race, _ = Race.objects.get_or_create(
            name=race_name,
            defaults={"description": race_description}
        )

        for skill_raw in race_raw.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_raw.get("name"),
                defaults={
                    "bonus": skill_raw.get("bonus"),
                    "race": race,
                }
            )

        guild = None
        guild_raw = item.get("guild")
        if guild_raw:
            guild, _ = Guild.objects.get_or_create(
                name=guild_raw.get("name"),
                defaults={"description": guild_raw.get("description", "")}
            )

        Player.objects.create(
            nickname=nickname,
            email=item.get("email"),
            bio=item.get("bio", ""),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
