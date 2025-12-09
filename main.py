import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as f:
        players_data = json.load(f)

    for nickname, player_json in players_data.items():

        # --- RACE ---
        race_data = player_json["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data.get("description", "")}
        )

        # --- SKILLS ---
        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race
                }
            )

        # --- GUILD ---
        guild_data = player_json.get("guild")
        guild = None
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data.get("description")}
            )

        # --- PLAYER ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": player_json["email"],
                "bio": player_json["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
