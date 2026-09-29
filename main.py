import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, pdata in players_data.items():
        race, _ = Race.objects.get_or_create(
            name=pdata["race"]["name"],
            defaults={"description": pdata["race"].get("description", "")}
        )

        for skill_data in pdata["race"].get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        guild = None
        if "guild" in pdata and pdata["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=pdata["guild"]["name"],
                defaults={
                    "description": pdata["guild"].get("description", "")
                }
            )

        Player.objects.get_or_create(
            nickname=pdata.get("nickname", nickname),
            defaults={
                "email": pdata.get("email", ""),
                "bio": pdata.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )

if __name__ == "__main__":
    main()
