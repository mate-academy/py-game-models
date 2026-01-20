import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", encoding="utf-8") as file:
        players_data = json.load(file)

    for nickname, data in players_data.items():
        # --- RACE ---
        race_data = data.get("race")
        race, _ = Race.objects.get_or_create(
            name=race_data.get("name"),
            defaults={
                "description": race_data.get("description")
            }
        )

        # --- SKILLS ---
        for skill_data in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill_data.get("name"),
                race=race,
                defaults={
                    "bonus": skill_data.get("bonus")
                }
            )

        # --- GUILD ---
        guild = None
        if data["guild"] is not None:
            guild_data = data.get("guild")
            guild, _ = Guild.objects.get_or_create(
                name=guild_data.get("name"),
                defaults={
                    "description": guild_data.get("description")
                }
            )

        # --- PLAYER ---
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": data.get("email"),
                "bio": data.get("bio"),
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()
