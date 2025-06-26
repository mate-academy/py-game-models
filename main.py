import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild
import json
from django.utils.timezone import now


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players = json.load(f)
    for nickname, player_data in players.items():
        race_data = player_data["race"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                race=race,
                defaults={"bonus": skill_data["bonus"]}
            )

        guild = None
        guild_data = player_data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
                "created_at": now()
            }
        )


if __name__ == "__main__":
    main()
