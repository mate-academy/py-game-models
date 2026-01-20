import json
from db.models import Race, Skill, Guild, Player
from django.utils.timezone import now


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        data = json.load(f)

    for nickname, entry in data.items():
        race, _ = Race.objects.get_or_create(
            name=entry["race"]["name"],
            defaults={"description": entry["race"].get("description", "")}
        )

        for skill_data in entry["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        guild_data = entry.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description", "")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": entry.get("email", ""),
                "bio": entry.get("bio", ""),
                "race": race,
                "guild": guild,
                "created_at": now()
            }
        )


if __name__ == "__main__":
    main()
