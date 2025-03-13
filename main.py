import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r", encoding="utf-8") as file:
        players_data = json.load(file)

    for player in players_data:
        race, _ = Race.objects.get_or_create(name=player["race"]["name"], defaults={
            "description": player["race"].get("description", "")
        })

        guild = None
        if "guild" in player and player["guild"]:
            guild, _ = Guild.objects.get_or_create(name=player["guild"]["name"], defaults={
                "description": player["guild"].get("description", "")
            })

        player_obj, _ = Player.objects.get_or_create(
            nickname=player["nickname"],
            defaults={
                "email": player.get("email", ""),
                "bio": player.get("bio", ""),
                "race": race,
                "guild": guild
            }
        )

        for skill_data in player.get("skills", []):
            skill, _ = Skill.objects.get_or_create(name=skill_data["name"], defaults={
                "bonus": skill_data["bonus"],
                "race": race
            })

if __name__ == "__main__":
    main()
