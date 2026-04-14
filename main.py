import init_django_orm  # noqa: F401
import json
from django.utils import timezone
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, pdata in players_data.items():
        race_data = pdata["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        guild = None
        if pdata.get("guild"):
            guild_data = pdata["guild"]
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": pdata["email"],
                "bio": pdata["bio"],
                "race": race,
                "guild": guild,
                "created_at": timezone.now()
            }
        )


if __name__ == "__main__":
    main()
