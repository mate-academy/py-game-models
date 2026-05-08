import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Guild, Player


def main() -> None:

    with open("players.json", "r") as f:
        player_data = json.load(f)

    for nickname, data in player_data.items():

        race_data = data["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        guild = None
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data["email"],
                "bio": data.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
